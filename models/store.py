from db import db
class model_store(db.Model):
    __tablename__="stores"

    id=db.Column(db.Integer, primary_key='True')
    name = db.Column(db.String(80))
    items=db.relationship('model_item') #it will understand that model_store has a relationship with model_item

    def __init__(self,name):
        self.name =name

    def json(self):
        return {'name':self.name, 'items':[item.json() for item in self.items ]}

    @classmethod
    def find_store(cls,name):
        return cls.query.filter_by(name=name).first()
        #select * from __table__ where name=name limit 1 (means return 1st row only)

    def up_sert(self):#this will do insert and update both because table has pri key id, if id found then update if not found insert

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
