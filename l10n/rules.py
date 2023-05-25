from l10n import bp_l10n
from flask_vue_robots.orm.db_model import TBUser, db
from tasks.asynchronous import send_report
from celery.result import AsyncResult
from flask import request, current_app

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

    with db.auto_commit():
        db.session.add(tf_user)
    return "OK"


@bp_l10n.get("/rule_detail")
def rule_detail():
    task: AsyncResult = send_report.apply_async(args=(12, 22))
    return task.id


@bp_l10n.post("/task")
def task_result():
    task_id:str = request.form.get("task_id")
    current_app.logger.warning(f"查看任务状态{task_id}")
    task: AsyncResult = send_report.AsyncResult(task_id)
    current_app.logger.warning(f"查看任务状态{task.result}")
    return "success"
