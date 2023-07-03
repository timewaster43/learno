from flask import Blueprint, render_template, redirect
import app

bp = Blueprint("student", __name__, url_prefix="/student")


@bp.route('/')
def index():
    if app.isLogin and app.auth == "student":
        return render_template("student.html")
    else:
        return redirect('/submit/error')
