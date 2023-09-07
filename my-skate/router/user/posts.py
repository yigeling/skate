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
            return generate_response(code=1)

api.add_resource(PostlikeView, "/userlike/<id>", endpoint="postid")

# class qiQiutest(Resource):
#     @auth_required
#     def post(self):
#         # 配置七牛云的相关参数
#         access_key = 'VXNY_oVAwVsXUfq1X8e3iH81lzLVIPdXO9eKRfzU'
#         secret_key = 'E--8ljmpTGoOa6ozzOOxIMNL8-r17S2S2rcA1NfN'
#         bucket_name = '7up'
#         qiniu_domain = ''
#         # 初始化
#         q = Auth(access_key, secret_key)
#         # 上传token
#         file = request.files['file']
#         if file:
#             # 生成上传 Token
#             token = q.upload_token(bucket_name)
#             # 上传文件到七牛云
#             ret, info = put_file(token, None, file.read())
#             if ret and ret.get('key'):
#                 # 构建图片 URL
#                 if qiniu_domain:
#                     image_url = f'{qiniu_domain}/{ret["key"]}'
#                 else:
#                     image_url = f'http://{bucket_name}.bkt.clouddn.com/{ret["key"]}'
#                 # 返回图片 URL
#                 return jsonify({'url': image_url})
#         return jsonify({'error': '上传失败'})
#
# api.add_resource(qiQiutest, "/test")

class qiQiutest(Resource):
    @auth_required
    def post(self):
        # 配置七牛云的相关参数
        access_key = 'VXNY_oVAwVsXUfq1X8e3iH81lzLVIPdXO9eKRfzU'
        secret_key = 'E--8ljmpTGoOa6ozzOOxIMNL8-r17S2S2rcA1NfN'
        bucket_name = '7up'
        qiniu_domain = 'rziyokt30.hn-bkt.clouddn.com'
        # 初始化
        q = Auth(access_key, secret_key)
        # 上传token
        file = request.files['file']
        if file:
            # 生成上传 Token
            token = q.upload_token(bucket_name)
            # 上传文件到七牛云
            ret, info = put_file(token, None, file.read())
            if ret and ret.get('key'):
                # 构建图片 URL
                if qiniu_domain:
                    image_url = f'{qiniu_domain}/{ret["key"]}'
                else:
                    image_url = f'http://{bucket_name}.bkt.clouddn.com/{ret["key"]}'
                # 返回图片 URL
                return jsonify({'url': image_url})
        return jsonify({'error': '上传失败'})

api.add_resource(qiQiutest, "/upload")