# 程序入口

from app import creat_app

skate_app = creat_app()

# @skate_app.route("/")
# def index():
#     return "skate app"

from flask_migrate import Migrate
from models import db

migrate = Migrate(skate_app, db)

if __name__ == '__main__':
    skate_app.run(host=skate_app.config['HOST'],
                port=skate_app.config['PORT'],
                debug=skate_app.config["DEBUG"])
