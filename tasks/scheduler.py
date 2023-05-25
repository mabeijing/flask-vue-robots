import time

from flask_vue_robots.extension.ext_celery import celery



@celery.task
def send_ok():
    time.sleep(3)

    return "OK"
