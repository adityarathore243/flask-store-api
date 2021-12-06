from models.user import UserModel

def authenticate(username,password):
    user=UserModel.find_username(username)
    if user and user.password==password:#passing this password inside postman body under /auth.in auth we dont need request.get_json
        return user

def identity(payload): #payload is a content of JWT token and extract userid from this payload
    user_id=payload['identity']
    return UserModel.find_id(user_id)
