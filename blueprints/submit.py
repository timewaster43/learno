from flask import Blueprint, redirect, request, render_template
import exts
from models import Teacher, Student
import app

bp = Blueprint("submit", __name__, url_prefix="/submit")


@bp.route('/login', methods=['POST'])
def submit():
    auth = request.form.get('auth')
    app.name = request.form.get('name')
    password = request.form.get('password')
    password = exts.encrypt(password)
    if auth == "student":
        result = Student.query.filter_by(name=app.name).first()
    else:
        result = Teacher.query.filter_by(name=app.name).first()
    if result and result.password == password:
        print(result.password)
        app.isLogin = True
        app.auth = auth
        return redirect('/login/success')
    else:
        return redirect('/login/wrong')


@bp.route("/error")
def error():
    situation = "submit"
    return render_template("wrong.html", situation=situation)