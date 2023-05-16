from flask import Flask
from l10n import bp_l10n

from tasks import celery_init_app
from flask_vue_robots.log import logging_init_app
from flask_vue_robots import config

# http://127.0.0.1:5000/images/1.txt
app = Flask(__name__, static_folder='../static', static_url_path='/images', template_folder='templates')

app.config.from_object(config.DevelopConfig)

logging_init_app(app)
celery_init_app(app)
app.register_blueprint(bp_l10n)


@app.get("/")
def index():
    app.logger.info("dcsdcsc")
    return "welcome to Hello World!"


@app.get("/run")
def run():
    pass
