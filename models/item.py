from db import db
class model_item(db.Model):
    __tablename__="items"

    id=db.Column(db.Integer, primary_key='True')
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id=db.Column(db.Integer, db.ForeignKey('stores.id'))
    store=db.relationship('model_store')

    def __init__(self,store_id,name,price):
        self.store_id=store_id
        self.name =name
        self.price= price

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def find_item(cls,name):
        return cls.query.filter_by(name=name).first()
        #select * from __table__ where name=name limit 1 (means return 1st row only)

    def up_sert(self):#this will do insert and update both because table has pri key id, if id found then update if not found insert

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
