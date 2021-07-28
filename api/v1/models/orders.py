from api.v1.models import db
class Order(db.Model):
    __tablename__ = 'pet'
    name = db.Column('name', db.String)




