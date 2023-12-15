import time

import httpx
from fastapi import APIRouter, Depends, HTTPException

from admin.content.api import getStock, updateProduct, getProduct
from admin.content.fabrica.fabrica import ensamblarProducto
from api_db.cruds.controllers.controllerProducts import get_product
from api_db.cruds.controllers.controllerProductsSales import create_product_sale
from api_db.cruds.controllers.controllerSales import create_sale
from api_db.cruds.controllers.controllerUsers import get_cart
from api_db.cruds.schemas.schemas import SaleCreate, ProductSaleCreate
from api_db.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime

from static.api import getCart, postSale, getUserWithToken, postProductSale

router = APIRouter()


@router.post("/api/order")
async def post_pedido(order_data: dict, db: Session = Depends(get_db)):
    user_id = order_data["user_id"]
    products = order_data["products"]
    print("Pedido de user ", user_id, " recibido: ", products)

    return await order(user_id, products, db)


@router.post("/api/clientes/order")
async def post_pedido(data: dict, db: Session = Depends(get_db)):
    token = data["token"]
    cart_response = await getCart(token)
    user_response = await getUserWithToken(token)

    user_id = ""
    products = []
    if cart_response["status"] == 200 and user_response["status"] == 200:
        user_id = user_response["data"]["id"]
        products = cart_response["data"]

    print("Pedido de user ", user_id, " recibido: ", products)

    return await order(user_id, products, db)


async def order(user_id, products, db):
    total = 0
    for product_data in products:
        product = await get_product(product_data["id"], db)
        total += product.price * product_data["quantity"]

    sale_data = {
        "user_id": user_id,
        "date": str(datetime.now()),
        "total": total,
        "props": {},
        "state_id": 1,
        "enabled": 1,
    }
    sale = await postSale(sale_data)

    for product_data in products:
        product = await get_product(product_data["id"], db)
        quantity = product_data["quantity"]
        subtotal = product.price * quantity

        # Verificar si hay suficiente stock del producto
        if product.stock < quantity:
            # Si no hay suficiente stock, fabricar la cantidad faltante
            await ensamblarProducto(product.id, quantity - product.stock, db)


        # Crear el registro en ProductSale
        product_sale_data = {
            "product_id": product.id,
            "sale_id": sale["id"],
            "quantity": quantity,
            "subtotal": subtotal,
            "enabled": 1,
        }

        await restar_stock_producto(product.id, quantity, db)

        await create_product_sale(ProductSaleCreate(**product_sale_data), db)

    return {"Message": "Pedido exitoso!, contamos con su pedido en stock, en seguida se le entregará"}


async def restar_stock_producto(product_id: int, quantity: int, db: Session):
    product = await get_product(product_id, db)
    if product.stock < quantity:
        raise HTTPException(status_code=400, detail="No hay suficiente stock para restar")

    product.stock -= quantity
    db.commit()


# @router.post("/api/order")
# async def post_pedido(data: dict):
#     token = data["token"]
#     cart_response = await getCart(token)
#     user_response = await getUserWithToken(token)
#
#     if cart_response["status"] == 200 and user_response["status"] == 200:
#         user = user_response["data"]
#         products = cart_response["data"]
#
#         total = 0
#
#         stock_requirement_done = True
#         products_to_build = []
#
#         # validar si stock cumple con el pedido
#         for product in products:
#             stock_response = await getStock(product["id"])
#             print("Stock response: ", stock_response)
#             product_stock = stock_response["stock"]
#             if product["quantity"] > product_stock:
#                 stock_requirement_done = False
#                 products_to_build.append({
#                     "id": product["id"],
#                     "name": product["name"],
#                     "needed_quantity": (product["quantity"] - product_stock)
#                 })
#
#         # Mandar a producir de ser necesario o entregar producto al cliente
#         if stock_requirement_done == False:
#             await sendToBuild(products_to_build)
#             return {"Message": "Pedido exitoso!, en este momento no se cuenta con la cantidad de producto solicitado,"
#                                " pero se le enviara a su domicilio"}
#         else:
#             for product in products:
#                 total += (product["price"] * product["quantity"])
#             total *= 1.16
#             fecha = datetime.now()
#             sale_data = {
#                 "date": fecha.strftime("%Y-%m-%d"),
#                 "total": total,
#                 "props": {},
#                 "enabled": 1,
#                 "user_id": user["id"],
#                 "state_id": 1,
#             }
#             sale_response = await postSale(sale_data)
#
#             for product in products:
#                 prod_sale_data = {
#                     "product_id": product["id"],
#                     "sale_id": sale_response["id"],
#                     "quantity": product["quantity"],
#                     "subtotal": (product["price"] * product["quantity"]),
#                     "props": {},
#                     "enabled": 1,
#                 }
#                 print(prod_sale_data)
#                 await postProductSale(prod_sale_data)
#
#                 # Actualizar el inventario
#                 product_stock_response = await getStock(product["id"])
#                 await updateProduct(product["id"], {
#                     "name": product["name"],
#                     "stock": (product_stock_response["stock"] - product["quantity"]),
#                 })
#
#             return {"Message": "Pedido exitoso!, contamos con su pedido en stock, en seguida se le entregará"}
#


@router.post("/api/products/plasticos")
def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " carcasas, manos a la obra\n\n")
    time.sleep(2)
    print("\n\nCalculando stock disponible\n\n")
    time.sleep(2)
    print("\n\nStock disponible, haciendo envio\n\n")

    return {"Mensaje": "Pedido exitoso"}
