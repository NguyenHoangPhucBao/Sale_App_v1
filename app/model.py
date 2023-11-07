from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app


class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship("Products", backref="category", lazy=True)


class Products(db.Model):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(255), unique=True)
    description = Column(String(70))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        pass

        # c1 = Category(name = "Mobile", id = 1)
        # c2 = Category(name = "Tablet")
        # c3 = Category(name = "Laptop")
        #
        # d1 = Products(name = "iPhone 7 Plus", price = 17000000, image = "images/ip7p.jpg", category_id = int(1), description = "Apple, 32GB, RAM: 3GB, iOS13")
        # d2 = Products(name = "iPad Pro 2020", price = 37000000, image = "images/ipadpro.jpg", category_id = int(2), description = "Apple, 128GB, RAM: 6GB")
        # d3 = Products(name = "Galaxy Note 10 Plus", price = 24000000, image = "images/gnote10p.jpg", category_id = int(1), description = "Samsung, 64GB, RAML: 6GB")
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.add_all([d1, d2, d3])
        # db.session.commit()

        # db.create_all()
