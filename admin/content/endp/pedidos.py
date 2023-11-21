import time

import httpx
from fastapi import APIRouter, Depends

from api_db.cruds.controllers.controllerSales import create_sale
from api_db.cruds.controllers.controllerUsers import get_cart
from api_db.cruds.schemas.schemas import SaleCreate
from api_db.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime

from static.api import getCart, postSale, getUserWithToken, postProductSale

router = APIRouter()


@router.post("/api/productss")
async def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " iphones\n\n")
    time.sleep(5)
    async with httpx.AsyncClient() as client:

        data = {
            "cantidad": data["cantidad"]
        }

        response = await client.post("http://localhost:8003/api/products/plasticos", json=data)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


@router.post("/api/order")
async def post_pedido(data: dict):
    token = data["token"]
    cart_response = await getCart(token)
    user_response = await getUserWithToken(token)

    if cart_response["status"] == 200 and user_response["status"] == 200:
        user = user_response["data"]
        products = cart_response["data"]

        total = 0
        for product in products:
            total += (product["price"] * product["quantity"])
        total *= 1.16
        fecha = datetime.now()
        sale_data = {
            "date": fecha.strftime("%Y-%m-%d"),
            "total": total,
            "props": {},
            "enabled": 1,
            "user_id": user["id"],
            "state_id": 1,
        }
        sale_response = await postSale(sale_data)

        # product_id: int
        # sale_id: int
        # quantity: int
        # subtotal: float
        # props: dict
        # enabled: bool

        for product in products:
            prod_sale_data = {
                "product_id": product["id"],
                "sale_id": sale_response["id"],
                "quantity": product["quantity"],
                "subtotal": (product["price"] * product["quantity"]),
                "props": {},
                "enabled": 1,
            }
            print(prod_sale_data)
            prod_sale = await postProductSale(prod_sale_data)


@router.post("/api/products/plasticos")
def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " carcasas, manos a la obra\n\n")
    time.sleep(2)
    print("\n\nCalculando stock disponible\n\n")
    time.sleep(2)
    print("\n\nStock disponible, haciendo envio\n\n")

    return {"Mensaje": "Pedido exitoso"}
