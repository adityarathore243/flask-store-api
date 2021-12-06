from flask_restful import Resource,  reqparse
from flask_jwt import jwt_required
from models.store import model_store

class Store(Resource):##class "c" must be in smaill case

    def get(self, name):
        store=model_store.find_store(name)
        if store:
            return store.json(), 200 if store else 404##here we dont need to write jsonify because flask_restful auto. does 200 if item is not None else 404 both are same
        return {'msg':'item not found'}

    def post(self,name):
        if model_store.find_store(str(name)):
            return {'msg':"this name {} already exists".format(name)}, 400#bad request
        store=model_store(name)
        store.up_sert()
        return store.json(),201 if store else 400

    def delete(self,name):
        store=model_store.find_store(name)
        if store is None:
            return ({'msg':"Item {} not exists".format(name)}), 400#bad request

        else:
            store.delete()
            return {'msg':'item deleted'}


class Stores(Resource):
    def get(self):
        stores=model_store.query.all()
        return {'stores':[x.json() for x in stores]}
