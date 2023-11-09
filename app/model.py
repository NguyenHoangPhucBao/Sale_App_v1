from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin
# import hashlib

class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    def __str__(self):
        return self.name


class Category(Base):
    __tablename__ = "category"
    products = relationship("Products", backref="category", lazy=True)


class Products(Base):
    __tablename__ = "products"
    price = Column(Float, default=0)
    image = Column(String(255))
    description = Column(String(70))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


class User(Base, UserMixin):
    __tablename__ = "users"
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    avatar = Column(String(255))



if __name__ == "__main__":
    with app.app_context():
        pass
        # db.create_all()
        # u = User(
        #     name="Admin",
        #     username="admin",
        #     password=str(hashlib.md5("admin".encode("utf-8")).hexdigest())
        # )
