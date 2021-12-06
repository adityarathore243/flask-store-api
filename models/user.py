from db import db
class UserModel(db.Model):
    __tablename__="users"

    id=db.Column(db.Integer, primary_key='True')#fiart letter should be capital Interger String
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))#its good all 3 columns should be declared below in __init__

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_username(cls,name):
        return cls.query.filter_by(username=name).first()

    @classmethod
    def find_id(cls,_id):
         return cls.query.filter_by(id=_id).first()
