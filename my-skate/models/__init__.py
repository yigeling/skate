# 绑定数据模型：
#  	models    flask-sqlalchemy   对象关系映射
#  	类  映射--》 表
#  	属性  --》 字段
#  	对象 --》 记录
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app_db(app):
    # 绑定app
    db.init_app(app)

from . import user
