import time

import httpx
from fastapi import APIRouter, Depends, HTTPException

from admin.content.api import getStock, updateProduct, getProduct
from api_db.cruds.controllers.controllerProducts import get_product
from api_db.cruds.controllers.controllerProductsSales import create_product_sale
from api_db.cruds.controllers.controllerSales import create_sale
from api_db.cruds.controllers.controllerUsers import get_cart
from api_db.cruds.schemas.schemas import SaleCreate, ProductSaleCreate
from api_db.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime

# from static.api import getCart, postSale, getUserWithToken, postProductSale

router = APIRouter()


# @router.post("/api/productss")
# async def post_pedido(data: dict):
#     print("\n\nPedido recibido por " + str(data["cantidad"]) + " iphones\n\n")
#     time.sleep(5)
#     async with httpx.AsyncClient() as client:
#
#         data = {
#             "cantidad": data["cantidad"]
#         }
#
#         response = await client.post("http://localhost:8003/api/products/plasticos", json=data)
#
#     if response.status_code == 200:
#         result = response.json()
#         return result
#     else:
#         return None
#
# @router.post("/api/products/plasticos")
# def post_pedido(order_data: dict, db: Session = Depends(get_db)):
#
#     create_sale(order_data, db)
#     print("\n\nPedido recibido por " + str(data["cantidad"]) + " carcasas, manos a la obra\n\n")
#     time.sleep(2)
#     print("\n\nCalculando stock disponible\n\n")
#     time.sleep(2)
#     print("\n\nStock disponible, haciendo envio\n\n")
#
#     return {"Mensaje": "Pedido exitoso"}


@router.post("/api/order")
async def post_pedido(order_data: dict, db: Session = Depends(get_db)):
    user_id = order_data["user_id"]
    products = order_data["products"]

    total = 0
    for product_data in products:
        # print("Product id: ", product_data["id"])
        product = await get_product(product_data["id"], db)
        # print(product)
        print(product.price)
        total += product.price * product_data["quantity"]

    sale_data = {
        "user_id": user_id,
        "date": str(datetime.now()),
        "total": total,
        "props": {},
        "state_id": 1,
        "enabled": 1,

    }
    sale = await create_sale(SaleCreate(**sale_data), db)

    for product_data in products:
        product = await get_product(product_data["id"], db)
        quantity = product_data["quantity"]
        subtotal = product.price * quantity
        product_sale_data = {
            "product_id": product.id,
            "sale_id": sale.id,
            "quantity": quantity,
            "subtotal": subtotal,
            "enabled": 1,
        }
        await create_product_sale(ProductSaleCreate(**product_sale_data), db)

    return {"Mensaje": "Pedido exitoso"}







