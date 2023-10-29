import json, os
from app import app

def read_json(path):
    with open(path, "r") as f:
        return  json.load(f)


def load_categories():
    return read_json(os.path.join(app.root_path, "data/Categories.json"))


def load_products(cate_id=None, kw=None, start_price=None, end_price=None):
    products = read_json(os.path.join(app.root_path, "data/products.json"))

    if cate_id:
        products = [p for p in products if p["category_id"] == int(cate_id)]

    if kw:
        products = [p for p in products if kw.lower() in p["name"].lower()]

    if start_price:
        products = [p for p in products if int(start_price) <= p["price"]]

    if end_price:
        products = [p for p in products if int(end_price) >= p["price"]]

    return products