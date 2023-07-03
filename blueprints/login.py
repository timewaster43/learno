from flask import Blueprint, render_template, redirect
import app

bp = Blueprint("login", __name__, url_prefix="/login")


@bp.route('/success')
def success():
    if app.isLogin:
        return render_template("success.html", name=app.name, auth=app.auth)
    else:
        return redirect('/login/wrong')


@bp.route('/wrong')
def wrong():
    app.isLogin = False
    app.auth = ''
    app.name = ''
    situation = "login"
    return render_template("wrong.html", situation=situation)
