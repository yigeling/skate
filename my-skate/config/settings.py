#
DEBUG = True
# 应用程序将监听来自所有网络接口的请求，包括本地主机和外部网络
HOST = "0.0.0.0"
PORT = 9000

# 数据库设置
DB_HOST = "192.168.50.254"
DB_USER = "skate_app"
DB_SCHEM = "keke"
DB_PORT = 3306
DB_PASS = "123456"

# orm数据库链接设置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://skate_app:123456@192.168.50.254:3306/keke?charset=utf8'

# 设置内部私钥
SECRET_KEY = "123456"
# 过期时间
EXPIRES_IN = 6000

MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# 七牛云

