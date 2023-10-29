import utils
from app import app
from flask import render_template, request


@app.route("/")
def main():
    cates = utils.load_categories()
    return render_template("index.html", categories = cates)


@app.route("/products")
def show_products():
    cate_id = request.args.get("category_id")
    kw = request.args.get("keyword")
    start_price = request.args.get("from_price")
    end_price = request.args.get("to_price")
    products = utils.load_products(cate_id, kw, start_price, end_price)
    return  render_template("products.html", products = products)


@app.route("/products/productid=<product_id>")
def product_detail(product_id):
    return "SAN PHAM %s" %product_id


if __name__ == "__main__":
    app.run(debug = True)