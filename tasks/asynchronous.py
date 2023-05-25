import time

from flask_vue_robots.extension.ext_celery import celery


@celery.task(bind=True)
def send_report(self, x, y):
    time.sleep(8)
    return x + y
