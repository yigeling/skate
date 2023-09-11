from . import user_bp
from flask_restful import Resource, Api
from flask import request,jsonify
from libs.response import generate_response
from models.user import User_post
from libs.auth import auth_required
from models import db
# from qiniu import Auth, put_file

api = Api(user_bp)

# 首页/home页面，不需要登录，进入就会请求后端，刷新动态
class UserpostsView(Resource):
    def get(self):
        result = User_post.query.all()
        if result:
            if isinstance(result, list):
                result2 = [dict(pro) for pro in result]
            else:
                result2 = dict(result)
            return generate_response(message="get success", code=0, data=result2)
        else:
            return generate_response(message="data empty", code=1001)

    # 发布动态页面，暂时只实现发布纯文字类型的动态
    # 需要登录
    @auth_required
    def post(self):
        username = request.json.get('username')
        content = request.json.get('data')
        id = request.json.get('id')
        if content:
            new_post = User_post(username=username,
                                 content=content,
                                 u_id=id,
                                 user_like=0)
            db.session.add(new_post)
            db.session.commit()
            return generate_response(code=0)
        else:
            return generate_response(code=1, message="post empty")

api.add_resource(UserpostsView, "/userposts")

# 用户点赞
class PostlikeView(Resource):
    @auth_required
    def get(self, id):
        if id:
            new = (User_post.query.filter_by(id=id).first()).user_like + 1
            print('old',(User_post.query.filter_by(id=id).first()).user_like)
            print('new',new)
            return generate_response(code=0, data=new)
        else:
            return generate_response(code=1, message="未登录")

api.add_resource(PostlikeView, "/userlike/<id>", endpoint="postid")

