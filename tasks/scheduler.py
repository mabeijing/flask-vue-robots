import time

from flask_vue_robots.extension.ext_celery import celery


@celery.task
def send_ok():
    time.sleep(3)
    celery.flask_app.logger.warning(f"flask_app=>{id(celery.flask_app)}")
    return "OK"
