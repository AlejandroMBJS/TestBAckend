from fastapi import FastAPI, HTTPException, Header
from models import Product, User
from crud import create_product, read_products, read_product, update_product, delete_product

app = FastAPI()

admin_token = "myadminsecrettoken"  # Token de administrador
read_only_token = "myreadonlytoken"  # Token de solo lectura


@app.post("/products/")
async def create_new_product(product: Product, token: str = Header(None)):
    if token != admin_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return create_product(product)


@app.get("/products/")
async def get_all_products(token: str = Header(None)):
    if token != admin_token and token != read_only_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return read_products()


@app.get("/products/{sku}")
async def get_product(sku: str, token: str = Header(None)):
    if token != admin_token and token != read_only_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    product = read_product(sku)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.put("/products/{sku}")
async def update_product_data(sku: str, updated_product: Product, token: str = Header(None)):
    if token != admin_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    product = read_product(sku)
    if product:
        return update_product(sku, updated_product)
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{sku}")
async def delete_product_data(sku: str, token: str = Header(None)):
    if token != admin_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    product = read_product(sku)
    if product:
        return delete_product(sku)
    raise HTTPException(status_code=404, detail="Product not found")
