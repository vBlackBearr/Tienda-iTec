import asyncio
import os
import time
import uuid

import aiohttp
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from admin.content.fabrica.fabrica2 import restar_stock_producto
from api_db.cruds.controllers.controllerProducts import get_product
from api_db.database import get_db, SessionLocal

from admin.content.api import getProduct, getRawMaterial, create_pedido_pendiente
import api_db.cruds.controllers.controllerPedidosPendientes as crud_sale
from api_db.cruds.models.models import Product, BOM
from dotenv import load_dotenv

load_dotenv()

home = os.getenv('HOME')

router = APIRouter()


async def ensamblarProducto(product_id: int, quantity: int, db: SessionLocal = Depends(get_db), sale_id: int = 0,
                            products=None):
    # Obtener el producto
    if products is None:
        products = []
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise Exception(f"Product with id {product_id} not found.")
    print("Ensamblando producto :", product.name, "   cantidad: ", quantity)
    # Obtener la lista de materiales necesarios para el producto
    bom_entries = db.query(BOM).filter(BOM.product_id == product_id).all()

    # Construir el arreglo de materiales para el pedido
    pedido_materiales = []
    for bom_entry in bom_entries:
        raw_material = bom_entry.raw_material
        required_quantity = bom_entry.quantity * quantity

        if raw_material.stock < required_quantity:
            # Agregar a la lista de materiales para el pedido
            print(raw_material.name, " agotado, se hará pedido")
            pedido_materiales.append({
                "raw_material_id": raw_material.id,
                "quantity": required_quantity - raw_material.stock
            })

    if pedido_materiales:
        await hacerPedido(pedido_materiales, sale_id, products)

    # Continuar con la producción y actualizar el stock de las materias primas y del producto ensamblado
    for bom_entry in bom_entries:
        raw_material = bom_entry.raw_material
        required_quantity = bom_entry.quantity * quantity

        raw_material.stock -= required_quantity
        db.commit()

    product.stock += quantity
    db.commit()
    print(f"Producto ensamblado con éxito: {quantity} unidades de {product.name}.")
    return f"Producto ensamblado con éxito: {quantity} unidades de {product.name}."


@router.post("/backend/entrada_pedidos")
async def entrada_pedidos(data: dict, db: Session = Depends(get_db)):

    # Eliminar el pedido pendiente que llegó
    crud_sale.delete_pedido_pendiente(db, data["venta_id"], data["pedido_id"])

    # Verificar si ya no hay más pedidos pendientes para esa venta
    pedidos_pendientes = crud_sale.read_pedido_pendiente(data["venta_id"], db)

    if not pedidos_pendientes:
        # No hay más pedidos pendientes, realizar el proceso de fabricación
        products = data["props"]
        for product_data in products:
            product = await get_product(product_data["id"], db)
            quantity = product_data["quantity"]
            await restar_stock_producto(product.id, quantity, db)

    return {"status": "Pedido procesado exitosamente.", "pedido_id": data["pedido_id"]}

async def hacerPedido(pedido_materiales, sale_id, products):
    pedidos = await sortPartnersYProducts(pedido_materiales)
    resultados_pedidos = []

    for pedido in pedidos:
        data = {
            "venta_id": sale_id,
            "api_comprador": home,
            "pedido_id": str(uuid.uuid4()),
            "user_id": pedido["user_id"],
            "products": pedido["products"]
        }
        async with aiohttp.ClientSession() as session:
            url = (pedido["api_endpoint"] + "/api/order")
            print("Haciendo pedido de", data, " a ", url)
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    resultados_pedidos.append({"status_code": 200, "data": result})
                    print("creando fabricacion pendiente de pedido")
                else:
                    resultados_pedidos.append(None)
                await create_pedido_pendiente({"venta_id": sale_id, "pedido_id": data["pedido_id"], "props": products})


    # Puedes devolver algo o no, según tus necesidades
    return {"status": "Pedido en proceso, espera la notificación de completado."}


async def sortPartnersYProducts(pedido_materiales):
    partners = set()

    # Obtener partners de cada material
    for material in pedido_materiales:
        data = await getRawMaterial(material["raw_material_id"])
        if data["status_code"] == 200:
            partner = data["data"]["raw_materials_partners"][0]["partner"]
            partners.add((partner["user_id"], partner["api_endpoint"]))

    # Inicializar la lista de pedidos agrupados por partner_id
    pedidos_agrupados = [{"user_id": partner_id, "api_endpoint": api_endpoint, "products": []} for
                         partner_id, api_endpoint in partners]

    # Llenar la lista de pedidos con los productos correspondientes
    for material in pedido_materiales:
        data = await getRawMaterial(material["raw_material_id"])
        if data["status_code"] == 200:
            raw_material_partner = data["data"]["raw_materials_partners"][0]
            partner = raw_material_partner["partner"]
            if raw_material_partner["min_order"] > material["quantity"]:
                product = {"id": material["raw_material_id"], "quantity": material["quantity"]}
            else:
                product = {"id": material["raw_material_id"], "quantity": raw_material_partner["min_order"]}

            # Encontrar el pedido correspondiente en la lista
            pedido = next((p for p in pedidos_agrupados if p["user_id"] == partner["user_id"]), None)

            # Agregar el producto al pedido
            if pedido:
                pedido["products"].append(product)

    return pedidos_agrupados
