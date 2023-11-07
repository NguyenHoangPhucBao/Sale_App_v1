from model import Category, Products


def load_categories():
    return Category.query.all()


def load_products(cate_id=None, kw=None, start_price=None, end_price=None):
    products = Products.query.all()

    if cate_id:
        products = Products.query.filter(Products.category_id == int(cate_id))

    if kw:
        products = Products.query.filter(Products.name.contains(kw))

    if start_price:
        products = Products.query.filter(Products.price.__gt__(start_price))

    if end_price:
        products = Products.query.filter(Products.price.__lt__(end_price))

    return products
