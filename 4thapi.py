from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from secure import authenticate, identity
from resources.user import user_register
from resources.item import Item,Items
from resources.store import Store,Stores
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='jose'
api = Api(app)
jwt= JWT(app,authenticate,identity)
#here JWT creates new endpoint i.e. /auth,when we call /auth we send it a username & password, then JWT send this Username password to authenticate function
#if it matched then return user, this user becomes sort of identity, then auth retrun JWT toekn which call identity function,if its done means JWT token is valid
@app.before_first_request# it will run before any type of request and create table if not exists
def create_tables():
    db.create_all()

api.add_resource(Stores,'/stores')
api.add_resource(Store,'/store/<string:name>')

api.add_resource(Items,'/items')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(user_register,'/register')

if __name__=='__main__':###while importing file it will execute our code first at last it will run app
    db.init_app(app)
    app.run(port=5000, debug=True)
