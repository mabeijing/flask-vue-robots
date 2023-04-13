from flask import render_template



def base_http_exception_handle(e):
    print(e)
    return render_template("error404.html")


def base_exception_handle(e):
    print(e)
    return "e"
