from flask import Config


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
    pass


class ProductionConfig(AbstractConfig):
    pass
