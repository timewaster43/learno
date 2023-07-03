# MySQL所在主机
HOSTNAME = "127.0.0.1"
# MySQL监听端口，安装时设定为3306
PORT = 3306
# 用户名
USER = "root"
# 用户密码
PASSWORD = "root"
# 所使用的数据库
DATABASE = "freedata1"

DB_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI

# 哈希加密盐
salt = "axi5Vh"
