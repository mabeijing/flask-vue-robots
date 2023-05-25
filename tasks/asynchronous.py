import time

from flask_vue_robots.extension.ext_celery import celery


@celery.task(bind=True)
def send_report(self, x, y):
    time.sleep(8)
    print(f"Task => {id(self)}")  # 多进程下，这里获取的是app的fork对象
    print(f"Celery => {self.app}")  # 多进程下，这里获取的是app的fork对象
    print(f"Flask => {id(self.app.flask_app)}")  # 多进程下，这里获取的是app的fork对象
    return x + y
