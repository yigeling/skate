# 核心对象的创建和设置

from flask import Flask
from libs.con_mysql import connect_mysql


def creat_app():
    # 创建核心对象
    skate_app = Flask(__name__)

    # 连接数据库
    skate_app.mysql_db = connect_mysql()

    # 读取配置文件
    skate_app.config.from_object('config.settings')

    import router
    # 将蓝图和app绑定
    router.init_app(skate_app)

    # 绑定数据模型
    import models
    models.init_app_db(skate_app)


    return skate_app