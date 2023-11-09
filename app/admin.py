from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app import app, db
from model import Category, Products
from flask_login import logout_user, current_user
from flask import redirect


admin = Admin(app=app, name="Quan tri ban hang", template_mode="bootstrap4")


class Logout_view(BaseView):
    @expose("/")
    def logout(self):
        logout_user()
        return redirect("/admin")


class Authenticated_view(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class Category_view(Authenticated_view):
    column_list = ["id", "name", "products"]
    edit_modal = True
    column_searchable_list = ["name", "id"]


class Product_view(Authenticated_view):
    column_list = ["id", "name", "price", "description"]
    edit_modal = True
    column_searchable_list = ["name", "id", "description"]
    column_filters = ["price", "name"]


class Stats_view(BaseView):
    @expose("/")
    def main(self):
        return self.render("admin/stats.html")


admin.add_view(Category_view(Category, db.session))
admin.add_view(Product_view(Products, db.session))
admin.add_view(Stats_view(name="Statistic"))
admin.add_view(Logout_view(name="logout"))
