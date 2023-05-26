import threading
import traceback
from contextlib import contextmanager

from flask import Blueprint, current_app, g, request, session, abort
from sqlalchemy.orm import scoped_session

from flask_vue_robots.models import User
from flask_vue_robots.orm.rbac import TBRoles, TBUsers

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
        abort(500, f"服务器内部异常, trace_id:{g.trace_id}")


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


@bp_user.post("/async")
def show_user():
    task_id = request.form.get("task_id")
    task = create_user.AsyncResult(task_id)

    return task.result


@bp_user.post("/role/add")
def add_role():
    data: dict = request.json

    register_data: dict = {
        "role_id": data.get("role_id"),
        "role_name": data.get("role_name"),
        "father_id": data.get("father_id")
    }

    current_app.logger.debug(f"trace_id: {g.trace_id} - {data}")
    TBRoles(**register_data).save()

    role: TBRoles = TBRoles.query.filter(TBRoles.role_id == data.get("role_id")).first()
    return role.to_dict()


@bp_user.get("/login")
def login():
    data: dict = request.json
    register_data: dict = {
        "username": data.get("username"),
        "password": data.get("password")
    }

@bp_user.post("/register")
def register():
    data: dict = request.json
    register_data: dict = {
        "username": data.get("username"),
        "password": data.get("password"),
        "nick_name": data.get("nick_name", ""),
        "email": data.get("email", ""),
        "avatar": data.get("avatar", ""),
        "role_id": data.get("role_id")
    }
    TBUsers(**register_data).save()
    u: TBUsers = TBUsers.query.filter(TBUsers.username == data.get("username")).first()
    return u.to_dict()
