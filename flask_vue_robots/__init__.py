from flask import Flask
from l10n import bp_l10n

from tasks import celery_init_app
from flask_vue_robots.extension import logging_init_app
from flask_vue_robots import config

import settings

# http://127.0.0.1:5000/images/1.txt
app = Flask(__name__, static_folder='../static', static_url_path='/images', template_folder='templates')

app.config.from_object(config.DevelopConfig)

log_config = {
    "time_rotate_file_name": settings.ROOT.joinpath("logs", "run.log"),
    "app.name": app.name,
    "app.level": "DEBUG"
}

logging_init_app(app, settings.ROOT.joinpath("logging.yaml"), kwargs=log_config)
celery_init_app(app)
app.register_blueprint(bp_l10n)


@app.get("/")
def index():
    app.logger.info("dcsdcsc")
    return "welcome to Hello World!"


@app.get("/run")
def run():
    pass
