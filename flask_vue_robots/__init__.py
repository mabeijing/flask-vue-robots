from flask import Flask, render_template
from l10n import bp_l10n
from flask_vue_robots.error_handles import base_exception_handle
from werkzeug.exceptions import HTTPException


# http://127.0.0.1:5000/images/1.txt
app = Flask(__name__, static_folder='../static', static_url_path='/images', template_folder='templates')
# app.config['SECRET_KEY'] = 'secret!'

app.register_blueprint(bp_l10n)



@app.errorhandler(Exception)
def error_handle(e):
    return render_template("error404.html")

app.register_error_handler(HTTPException, base_exception_handle)