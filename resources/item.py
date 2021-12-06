from flask_restful import Resource,  reqparse
from flask_jwt import jwt_required
from models.item import model_item

class Item(Resource):##class "c" must be in smaill case
    parser=reqparse.RequestParser()#request is useful because its deal with argument which we defined here. if we no use it then it will update name as well price in line 55
    parser.add_argument('price',
    type=float,
    required=True,
    help="this can not left blank")
    parser.add_argument('store_id',
    type=int,
    required=True,
    help="this can not left blank")

    @jwt_required()
    def get(self, name):
        item=model_item.find_item(name)
        if item:
            return item.json(), 200 if item else 404##here we dont need to write jsonify because flask_restful auto. does 200 if item is not None else 404 both are same
        return {'msg':'item not found'}

    def post(self,name):
        if model_item.find_item(str(name)):
            return {'msg':"this name {} already exists".format(name)}, 400#bad request
        request_data=Item.parser.parse_args()
        item=model_item(request_data['store_id'],name,request_data['price'])
        item.up_sert()
        return item.json(),201 if item else 400

    def delete(self,name):
        item=model_item.find_item(name)
        if item is None:
            return ({'msg':"Item {} not exists".format(name)}), 400#bad request

        else:
            item.delete()
            return {'msg':'item deleted'}

    def put(self,name):
        request_data=Item.parser.parse_args()
        item=model_item.find_item(name)

        if item:
            item.price=request_data['price']

        else:
            item=model_item(request_data['store_id'],name,request_data['price'])

        item.up_sert()
        return item.json()

class Items(Resource):
    def get(self):
        items=model_item.query.all()
        return {'items':[x.json() for x in items]}
