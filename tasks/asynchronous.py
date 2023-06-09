import time

from flask_vue_robots.extension.ext_celery import celery
from flask_vue_robots.orm.db_model import db, TBUser


@celery.task(bind=True)
def send_report(self, x, y):
    time.sleep(8)
    print(f"Task => {id(self)}")  # 多进程下，这里获取的是app的fork对象
    print(f"Celery => {self.app}")  # 多进程下，这里获取的是app的fork对象
    print(f"Flask => {id(self.app.flask_app)}")  # 多进程下，这里获取的是app的fork对象
    return x + y


@celery.task(bind=True)
def create_user(self, username):
    tf_user = TBUser(username=username, email='58149278@qq.com')
    with self.app.flask_app.app_context():  # 涉及数据库操作的，需要在app_context()上下文中，操作模型无需在上下文
        with db.auto_commit():
            db.session.add(tf_user)

        user = TBUser.query.first()
    if user:
        return user.email
    return "NO EXIST"