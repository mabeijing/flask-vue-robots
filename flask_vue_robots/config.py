from flask import Config
from sqlalchemy import URL


class AbstractConfig(Config):
    DEBUG = False
    TESTING = True
    SECRET_KEY = "1a691f52d219228a1e1dcf57dd7ff84f5a1948690acb10571bbb97f4814fb873"
    SESSION_COOKIE_NAME = "session"
    PERMANENT_SESSION_LIFETIME = True
    MAX_CONTENT_LENGTH = 65535
    MAX_COOKIE_SIZE = 4093
    CELERY = dict(broken_url="redis://localhost", result_backend="redis://localhost", task_ignore_result=True)


class DevelopConfig(AbstractConfig):
    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = True
    MAX_COOKIE_SIZE = 4096

    """
    Flask-SQLAlchemy相关的配置
    - :data:`.SQLALCHEMY_DATABASE_URI`
    - :data:`.SQLALCHEMY_ENGINE_OPTIONS`
    - :data:`.SQLALCHEMY_ECHO`
    - :data:`.SQLALCHEMY_BINDS`
    - :data:`.SQLALCHEMY_RECORD_QUERIES`
    - :data:`.SQLALCHEMY_TRACK_MODIFICATIONS`
    """
    SQLALCHEMY_DATABASE_URI = URL.create(
        drivername="mysql+pymysql",
        username="root",
        password="root@123",
        host="localhost",
        port=3306,
        database="flask-vue-robots",
    )
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_BINDS = {
        "db1": URL.create(
            drivername="mysql+pymysql",
            username="root",
            password="root@123",
            host="localhost",
            port=3306,
            database="flask-vue-robots"),
        "db2": URL.create(
            drivername="mysql+pymysql",
            username="root",
            password="root@123",
            host="localhost",
            port=3306,
            database="tms_db")
    }


class ProductionConfig(AbstractConfig):
    pass
