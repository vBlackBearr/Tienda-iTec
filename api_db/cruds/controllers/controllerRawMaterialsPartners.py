from fastapi import APIRouter, Depends, HTTPException
from api_db.database import get_db, SessionLocal
# from admin.content.cruds.schemas.schemas import ProductCreate, ProductUpdate
from api_db.cruds.models.models import RawMaterialPartner

router = APIRouter()


@router.get("/raw_materials_partners")
def get_raw_materials_partners(skip: int = 0, limit: int = 10, db: SessionLocal = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


@router.post("/raw_materials_partners")
def create_raw_materials_partners(product: dict, db: SessionLocal = Depends(get_db)):
    db_product = RawMaterial(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/raw_materials_partners/{product_id}")
def get_product(product_id: int, db: SessionLocal = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/raw_materials_partners/{product_id}")
def update_product(product_id: int, product_data: ProductUpdate, db: SessionLocal = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for field, value in product_data.dict(exclude_unset=True).items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)
    return product


@router.delete("/raw_materials_partners/{product_id}")
def delete_product(product_id: int, db: SessionLocal = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return True
