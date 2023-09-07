from . import db
import datetime
from werkzeug.security import generate_password_hash

# 用户信息表表
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    # orm的password映射成数据库里的password字段，不知道的话则和orm名称一样
    _password = db.Column("password", db.String(128), nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.datetime.now)

    # posts = db.relationship("User_post", back_populates="author")

    __table_args__ = {
        'mysql_charset': 'utf8'
    }
    # property  python内置装饰器  属性包装装饰器
    # 作用： 把方法当作属性一样使用
    # 定义属性之前可以做一些检测、转换
    @property
    def password(self):
        return self._password
    # user.passwowrd()  --> print(user.password)

    @password.setter
    def password(self, value):
        # 在setter方法中可以添加逻辑来验证或处理属性值
        self._password = generate_password_hash(value)

    @classmethod    # 类方法 第一个参数代表类本身
    def create_user(cls, username, password):
        user = cls()    # 创建实例对象
        user.username = username
        user.password = password  # 调用password.setter装饰的函数，强制性要求存hash值
        db.session.add(user)
        db.session.commit()

class User_info(db.Model):
    __tablename__ = "user_info"
    # 在创建用户时同时在这张表里新增了一条信息，id一致
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), db.ForeignKey('user.username'), nullable=False, unique=True)
    sex = db.Column(db.String(128), nullable=True)
    photo = db.Column(db.String(128), nullable=True)
    signature = db.Column(db.String(128), nullable=True)
    age = db.Column(db.Integer, nullable=True)

    u_info = db.relationship("User_post", backref="info")

    __table_args__ = {
        'mysql_charset':'utf8'
    }

class User_post(db.Model):
    __tablename__ = "user_post"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    username = db.Column(db.String(128))
    head = db.Column(db.Integer, default=0)
    content = db.Column(db.String(128), nullable=True)
    photo = db.Column(db.String(128), nullable=True)
    user_like = db.Column(db.Integer, nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.datetime.now)

    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    # 可以通过dict函数将对象变成字典。 对象要实现 keys 和 __getitem__的方法
    # dict函数转化字典的时候，自动调用对象中keys方法，定义字典中的key
    # 然后依照字典的取值方法(__getietm__)去获取对应的key的值
    def keys(self):
        return ('id','u_id','username', 'head', 'content', 'photo', 'user_like', 'add_time')

    def __getitem__(self, item):
        if item == 'add_time':
            return getattr(self, item).strftime('%Y-%m-%d %H:%M:%S')
        elif item == 'head':
            return self.info.photo
        else:
            return getattr(self, item)