import utils
from app import app, login, encrypt
from flask import render_template, request, redirect
from flask_login import login_user
from model import User

@app.route("/")
def main():
    cates = utils.load_categories()
    return render_template("index.html", categories=cates)


@app.route("/products")
def show_products():
    cate_id = request.args.get("category_id")
    kw = request.args.get("keyword")
    start_price = request.args.get("from_price")
    end_price = request.args.get("to_price")
    products = utils.load_products(cate_id, kw, start_price, end_price)
    return render_template("products.html", products=products)


@app.route("/products/productid=<product_id>")
def product_detail(product_id):
    return "SAN PHAM %s" % product_id


@login.user_loader
def get_user(user_id):
    return utils.get_user_by_id(user_id)


@app.route("/admin/login", methods=["post"])
def admin_login():
    username = request.form.get("username")
    password = request.form.get("password")
    user=User.query.filter_by(username=username).first()
    if user.password == encrypt(password):
        login_user(user=user)
    return redirect("/admin")


if __name__ == "__main__":
    from app import admin
    app.run(debug=True)
