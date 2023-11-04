from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from api_db.database import get_db
from api_db.cruds.schemas.schemas import User, UserCreate, ValidUser
from api_db.cruds.models.models import User

# Token
import jwt
import os
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

router = APIRouter()

private_key_path = "api_db/private/private_key.pem"
public_key_path = "api_db/private/public_key.pem"

# Verificar si las claves existen
if not (os.path.exists(private_key_path) and os.path.exists(public_key_path)):
    # Las claves no existen, generarlas
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Guardar las claves en archivos
    with open(private_key_path, "wb") as private_file:
        private_file.write(private_pem)

    with open(public_key_path, "wb") as public_file:
        public_file.write(public_pem)
else:
    # Las claves ya existen, cargarlas desde los archivos
    with open(private_key_path, "rb") as private_file:
        private_pem = private_file.read()

    with open(public_key_path, "rb") as public_file:
        public_pem = public_file.read()


# Define una función para generar tokens JWT
def generate_jwt_token(data, expiration_minutes=30):
    payload = {
        "data": data,
        "exp": datetime.utcnow() + timedelta(minutes=expiration_minutes)
    }
    token = jwt.encode(payload, private_pem, algorithm='RS256')
    return token


@router.post("/backend/login")
def create_session(user: ValidUser, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user.email).filter(User.password == user.password).first()
    if not user:
        return {"Message": "Username or password incorrect"}
    else:

        token = generate_jwt_token({"user_id": 123})

        return {"user": user, "token": token}


@router.get("/protected")
def protected_route(Authorization: Annotated[str | None, Header()] = None):
    token = Authorization

    try:
        payload = jwt.decode(token, public_pem, algorithms=['RS256'])
        user_id = payload['data']['user_id']
        return f"User ID: {user_id}"
    except jwt.ExpiredSignatureError:
        return "Token expirado", 401
    except jwt.InvalidTokenError:
        return "Token inválido", 401


@router.get("/backend/users")
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@router.post("/backend/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/backend/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/backend/users/{user_id}")
def update_user(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in user_data.dict(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


@router.delete("/backend/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return True
