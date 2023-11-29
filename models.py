from pydantic import BaseModel


class Product(BaseModel):
    sku: str
    name: str
    price: float
    brand: str


class User(BaseModel):
    username: str
    password: str
    is_admin: bool = False
