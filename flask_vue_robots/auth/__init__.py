import threading
import traceback
from contextlib import contextmanager

from flask import Blueprint, current_app, g
from sqlalchemy.orm import scoped_session

from flask_vue_robots.models import User
from flask_vue_robots.orm.db_model import db, TBUser
from tasks.asynchronous import create_user

bp_user = Blueprint('bp_user', __name__, url_prefix='/user')


@contextmanager
def session_scoped():
    session = scoped_session(current_app.extensions["sessionmaker"])
    current_app.logger.warning(f"thread=>{threading.current_thread()} and session=>{id(session)}")
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        current_app.logger.error(f"trace_id:{g.trace_id} {traceback.format_exc(chain=False)}")


@bp_user.get("/add_user/<int:user_id>")
def add_user(user_id: int):
    with session_scoped() as session:
        user = User(name=str(user_id), fullname="mabeijing")
        session.add(user)
    return "OK"

@bp_user.post("/async_add/<username>")
def async_add_user(username):
    task = create_user.apply_async(args=(username,))
    return task.id