from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from static.cruds.database import get_db, SessionLocal
from static.cruds.models.models import Rol

router = APIRouter()


@router.get("/backend/roles")
def get_roles(skip: int = 0, limit: int = 10, db: SessionLocal = Depends(get_db)):
    roles = db.query(Rol).offset(skip).limit(limit).all()
    return roles


@router.post("/backend/roles")
def create_rol(rol_data: dict, db: Session = Depends(get_db)):
    new_rol = Rol(**rol_data)
    db.add(new_rol)
    db.commit()
    db.refresh(new_rol)
    return new_rol


@router.get("/backend/roles/{rol_id}")
def get_rol(rol_id: int, db: Session = Depends(get_db)):
    rol = db.query(Rol).filter(Rol.id == rol_id).first()
    if not rol:
        raise HTTPException(status_code=404, detail="Rol not found")
    return rol


@router.put("/backend/roles/{rol_id}")
def update_rol(rol_id: int, rol_data: dict, db: Session = Depends(get_db)):
    rol = db.query(Rol).filter(Rol.id == rol_id).first()
    if not rol:
        raise HTTPException(status_code=404, detail="Rol not found")

    for field, value in rol_data.items():
        setattr(rol, field, value)

    db.commit()
    db.refresh(rol)
    return rol


@router.delete("/backend/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Rol).filter(Rol.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Rol not found")

    db.delete(role)
    db.commit()

    return {"message": "Rol deleted"}


