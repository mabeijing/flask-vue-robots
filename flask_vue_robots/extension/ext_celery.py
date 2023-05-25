import time

from celery import Celery
from celery.schedules import crontab


class FlaskCelery(Celery):

    def __init__(self, flask_app=None, main=None, loader=None, backend=None,
                 amqp=None, events=None, log=None, control=None,
                 set_as_current=True, tasks=None, broker=None, include=None,
                 changes=None, config_source=None, fixups=None, task_cls=None,
                 autofinalize=True, namespace=None, strict_typing=True, **kwargs):
        super().__init__(main, loader, backend, amqp, events, log, control, set_as_current, tasks, broker,
                         include, changes, config_source, fixups, task_cls, autofinalize, namespace, strict_typing,
                         **kwargs)
        self.flask_app = flask_app

    def init_app(self, flask_app):
        self.flask_app = flask_app


# redis://:username:passowrd@host:port/db
celery = FlaskCelery(__name__, broker="redis://:root@123@localhost:6379/0",
                     backend="redis://:root@123@localhost:6379/1")

celery.conf.timezone = "Asia/Shanghai"

# 其实是importlib.import_module(),从项目跟路径开始
celery.conf.imports = ['tasks']

celery.conf.beat_schedule = {
    # task路径必须是可以import的
    "send_ok": {
        "task": "tasks.scheduler.send_ok",
        'schedule': crontab(minute="*/1")
    }
}


# 这里的可以直接扫描成task
@celery.task(bind=True)
def demo_task(self, x, y):
    time.sleep(4)
    return x + y
