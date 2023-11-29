from bson import ObjectId
from pymongo import MongoClient
from models import Product

# Initialize MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['catalog']
products_collection = db['products']


def create_product(product: Product):
    return products_collection.insert_one(product.dict())


def read_products():
    return list(products_collection.find({}))


def read_product(sku: str):
    return products_collection.find_one({"sku": sku})


def update_product(sku: str, updated_product: Product):
    return products_collection.update_one({"sku": sku}, {"$set": updated_product.dict()})


def delete_product(sku: str):
    return products_collection.delete_one({"sku": sku})
