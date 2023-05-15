from flask import Flask, render_template
from l10n import bp_l10n
from flask_vue_robots.error_handles import base_exception_handle
from werkzeug.exceptions import HTTPException
from tasks import celery_init_app

import importlib


# http://127.0.0.1:5000/images/1.txt
app = Flask(__name__, static_folder='../static', static_url_path='/images', template_folder='templates')

cfg = importlib.import_module(f"{__package__}.settings")
app.config.from_object(cfg.DevelopConfig)

celery_init_app(app)
app.register_blueprint(bp_l10n)


@app.get("/")
def index():
    app.logger.info("dcsdcsc")
    return "welcome to Hello World!"


@app.get("/run")
def run():
    pass


@app.errorhandler(Exception)
def error_handle(e):
    return render_template("error404.html")


app.register_error_handler(HTTPException, base_exception_handle)
