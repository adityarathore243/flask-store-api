from flask_restful import Resource, Api, reqparse
from models.user import UserModel

class user_register(Resource):
    parser=reqparse.RequestParser()#request is useful because its deal with argument which we defined here. if we no use it then it will update name as well price in line 55
    parser.add_argument('username',
    type=str, #type should be str int float
    required=True,
    help="this can not left blank")
    parser.add_argument('password',
    type=str,
    required=True,
    help="this can not left blank")

    def post(self):
        data=user_register.parser.parse_args()
        user=UserModel.find_username(data['username'])
        if user is None:
            user=UserModel(data['username'],data['password'])
            user.insert()
            return {'msg':'User Created Successfully'}
        else:
            return {'msg':'User already Exists'}
