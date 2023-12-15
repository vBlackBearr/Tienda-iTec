from fastapi import HTTPException
from sqlalchemy.orm import Session

from api_db.cruds.controllers.controllerProducts import get_product


async def restar_stock_producto(product_id: int, quantity: int, db: Session):
    product = await get_product(product_id, db)
    if product.stock < quantity:
        raise HTTPException(status_code=400, detail="No hay suficiente stock para restar")

    product.stock -= quantity
    db.commit()