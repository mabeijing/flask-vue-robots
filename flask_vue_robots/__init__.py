import uuid

from flask import Flask, g
from l10n import bp_l10n
from flask_vue_robots.auth import bp_user

from tasks import celery_init_app
from flask_vue_robots.extension import logging_init_app, sqlalchemy_init_app
from flask_vue_robots import config
from flask_vue_robots.orm import db

import settings

# http://127.0.0.1:5000/images/1.txt
app = Flask(__name__, static_folder='../static', static_url_path='/images', template_folder='templates')

app.config.from_object(config.DevelopConfig)

db.init_app(app)
log_config = {
    "time_rotate_file_name": settings.ROOT.joinpath("logs", "run.log"),
    "app.name": app.name,
    "app.level": "DEBUG"
}

logging_init_app(app, settings.ROOT.joinpath("logging.yaml"), kwargs=log_config)
sqlalchemy_init_app(app)
celery_init_app(app)
app.register_blueprint(bp_l10n)
app.register_blueprint(bp_user)


@app.before_request
def before_request():
    g.trace_id = str(uuid.uuid4())


with app.app_context():
    db.create_all()


@app.get("/")
def index():
    app.logger.info("dcsdcsc")
    return "welcome to Hello World!"
