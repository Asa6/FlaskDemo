
class Base(object):
    pass


class Mysql(object):
    HOST = '47.95.0.177'
    PORT = '3306'
    DATABASE = 'FlaskDemo'
    USERNAME = 'cmdb_hy'
    PASSWORD = 'iowkduw123'

    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class Config(Base, Mysql):
    pass
