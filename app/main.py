from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.base import get_db
from schemas.product import ProductCreate, ProductResponse

# 10

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/products")
def get_products(db:Session = Depends(get_db)):
    pass

@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db:Session = Depends(get_db)):
    pass

@app.post("/products")
def create_product(product: ProductCreate):
    pass
