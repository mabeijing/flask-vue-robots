import traceback
from datetime import datetime
from contextlib import contextmanager

import sqlalchemy as sa
from flask import current_app, g, abort
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()  # 事务
        except Exception as e:
            self.session.rollback()  # 回滚

            # 这样有一个好处，就是不需要引用traceback。也有一个坏处，无法过滤异常
            # current_app.logger.error("执行异常", exc_info=e)

            # 这样的话，异常也会是上色。支持异常过滤。比较推荐
            current_app.logger.error(f"trace_id:{g.trace_id}\n{traceback.format_exc(chain=False)}")
            abort(500, f"服务器内部异常, trace_id:{g.trace_id}")


db: _SQLAlchemy = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    is_deleted = sa.Column(sa.Boolean, name="IS_DELETED", default=False, comment="逻辑删除")
    create_time = sa.Column(sa.DateTime, name="CREATE_TIME", default=datetime.now, comment="创建时间")
    update_time = sa.Column(sa.DateTime, name="UPDATE_TIME", default=datetime.now, comment="更新时间")

    def save(self):
        with db.auto_commit():
            db.session.add(self)