from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api_db.cruds.models import models
from api_db.cruds.schemas import schemas
from api_db.database import get_db

router = APIRouter()


def delete_sale_pendiente(sale_id: int, pedido_id: str, db: Session = Depends(get_db)):
    db_pedido = db.query(models.PedidoPendiente).filter(models.PedidoPendiente.venta_id == sale_id).filter(models.PedidoPendiente.pedido_id == pedido_id).first()
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido Pendiente not found")

    db.delete(db_pedido)
    db.commit()

@router.post("/backend/pedidos_pendientes")
def create_pedido_pendiente(pedido: dict, db: Session = Depends(get_db)):
    db_pedido = models.PedidoPendiente(**pedido)
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido


@router.get("/backend/pedidos_pendientes/{pedido_id}")
def read_pedido_pendiente(pedido_id: str, db: Session = Depends(get_db)):
    db_pedido = db.query(models.PedidoPendiente).filter(models.PedidoPendiente.pedido_id == pedido_id).first()
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido Pendiente not found")
    return db_pedido


@router.get("/backend/pedidos_pendientes")
def read_pedidos_pendientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pedidos = db.query(models.PedidoPendiente).offset(skip).limit(limit).all()
    return pedidos


@router.put("/backend/pedidos_pendientes/{pedido_id}")
def update_pedido_pendiente(pedido_id: str, pedido: dict, db: Session = Depends(get_db)):
    db_pedido = db.query(models.PedidoPendiente).filter(models.PedidoPendiente.pedido_id == pedido_id).first()
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido Pendiente not found")

    for key, value in pedido.items():
        setattr(db_pedido, key, value)

    db.commit()
    db.refresh(db_pedido)
    return db_pedido


@router.delete("/backend/pedidos_pendientes/{pedido_id}")
def delete_pedido_pendiente(pedido_id: str, db: Session = Depends(get_db)):
    db_pedido = db.query(models.PedidoPendiente).filter(models.PedidoPendiente.pedido_id == pedido_id).first()
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido Pendiente not found")

    db.delete(db_pedido)
    db.commit()

    return {"message": "Pedido Pendiente deleted"}
