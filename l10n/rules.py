from l10n import bp_l10n



@bp_l10n.get("/")
def rules():
    # 这样会直接在浏览器执行js
    # 两种解决办法
    # 1 from flask import escape 转义
    # 2 直接用jinja2
    return '<script>alert("bad")</script>'

