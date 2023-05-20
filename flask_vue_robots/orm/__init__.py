import traceback
from contextlib import contextmanager

from flask import current_app, g
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


db = SQLAlchemy()
