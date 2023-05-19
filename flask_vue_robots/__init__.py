from flask import Flask
from l10n import bp_l10n

from tasks import celery_init_app
from flask_vue_robots.extension import logging_init_app
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
celery_init_app(app)
app.register_blueprint(bp_l10n)

with app.app_context():
    db.create_all()


@app.get("/")
def index():
    app.logger.info("dcsdcsc")
    return "welcome to Hello World!"


@app.get("/run")
def run():
    pass


from .models import User


@app.get("/add_user")
def add_user():
    from sqlalchemy.engine import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy import URL

    url_object = URL.create(
        "mysql+pymysql",
        username="root",
        password="root@123",
        host="localhost",
        port=3306,
        database="flask-vue-robots",
    )
    engine = create_engine(url_object, pool_recycle=3600, echo=True)

    session = Session(engine)

    user = User(name="beijing", fullname="mabeijing")
    session.add(user)
    session.commit()
    return "OK"
