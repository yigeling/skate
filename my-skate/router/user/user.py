from . import user_bp
from flask_restful import Resource, Api
from flask import request
from models.user import User, User_info
from libs.response import generate_response
from Form.user import UserForm, LoginForm
from libs.auth import create_token, auth_required
from models import db

# 蓝图和api的绑定
api = Api(user_bp)


class UserRegister(Resource):
    # 用户注册
    def post(self):
        data = request.json
        form = UserForm(data=data)
        if form.validate():
            User.create_user(
                username=data.get("username"),
                password=form.password.data)
            user_info = User_info(name=data.get("username"))
            # 用户注册时，同时添加用户资料表里的信息
            db.session.add(user_info)
            db.session.commit()
            return generate_response(message="注册成功", code=0)
        else:
            return generate_response(code=1, message=form.errors)

    # 获取用户资料
    @auth_required
    def get(self, username):
        result = User_info.query.filter_by(name=username).first()
        if result:
            print(result)
            return generate_response(message="success", code=0, data={
                "username": result.name,
                "sex": result.sex,
                "intro": result.signature,
                "avator": result.photo,
                "age": result.age,
            })
        else:
            return generate_response(message="fail", code=1)

api.add_resource(UserRegister, "/user")
api.add_resource(UserRegister, "/user/<username>", endpoint="userinfo")


# 登录视图
class LoginView(Resource):
    def post(self):
        data = request.json
        form = LoginForm(data=data)
        user = form.validate()
        if user:
            # 验证通过，生成token
            token = create_token(user.id)
            # print(token)
            # print(user.id)
            return generate_response(message="login success", code=0, data={"token": token,
                                                                            "username": user.username,
                                                                            "user_id": user.id})
        else:
            return generate_response(message="login fail", code=1)

api.add_resource(LoginView, "/login")


# 用户获取个人资料
# class InfoView(Resource):
#     def get(self, username):
#         result = User_info.query.filter_by(name=username).first()
#         if result:
#             print(result)
#             return generate_response(message="success", code=0, data={
#                 "username": result.name,
#                 "sex": result.sex,
#                 "intro": result.signature,
#                 "avator": result.photo,
#                 "age": result.age,
#             })
#         else:
#             return generate_response(message="fail", code=1)
#
# api.add_resource(InfoView, "/userinfo/<username>", endpoint="userinfo")

# # 退出登录
class Logout(Resource):
    def get(self):
        data = request.headers.get("token")
        if data:
            return True
        else:
            return False
#
api.add_resource(Logout, "/logout")


class token_verify(Resource):
    @auth_required
    def get(self):
        return generate_response(code=0)
api.add_resource(token_verify, "/token_verify")