from l10n import bp_l10n
from flask_vue_robots.orm.db_model import TBUser, db


@bp_l10n.get("/")
def rules():
    # 这样会直接在浏览器执行js
    # 两种解决办法
    # 1 from flask import escape 转义
    # 2 直接用jinja2
    return '<script>alert("bad")</script>'


@bp_l10n.get("/add_rule/<rule_name>")
def add_rule(rule_name):
    tf_user = TBUser(username=rule_name, email='58149278@qq.com')
    db.session.add(tf_user)
    db.session.commit()
    return "OK"