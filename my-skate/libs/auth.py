from flask import current_app, request
import time
import jwt
from jwt.exceptions import ExpiredSignatureError,InvalidSignatureError
from datetime import datetime
from libs.response import generate_response

def auth_required(func):
    def inner(*args, **kwargs):
        if token_auth():
            return func(*args, **kwargs)
        else:
            # return "token验证失败"
            return generate_response(code=1002, message="token验证失败")
    return inner

# 生成token
def create_token(uid):
    #生成token
    expir_in = current_app.config.get("EXPIRES_IN")
    payload = {"uid": uid, "exp": time.time() + expir_in}
    # print(payload)
    key = current_app.config["SECRET_KEY"]
    token = jwt.encode(payload, key)
    return token


#验证token
def token_auth():
    token = request.headers.get("token")
    if token:
        try:
            print(time.time(), datetime.now())
            jwt_obj = jwt.decode(token, current_app.config.get("SECRET_KEY"),
                                 algorithms=["HS256"])
        except InvalidSignatureError as e:
            print("token不合法", e)
            return False
        except ExpiredSignatureError as e:
            print("token过期", e)
            return False
        return True
    else:
        return False