from typing import TYPE_CHECKING

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from sqlalchemy import URL

if TYPE_CHECKING:
    from flask import Flask

url_object = URL.create(
    "mysql+pymysql",
    username="root",
    password="root@123",
    host="localhost",
    port=3306,
    database="flask-vue-robots",
)

engine = create_engine(url_object, pool_recycle=3600, echo=True)


def sqlalchemy_init_app(app: "Flask"):
    pass
