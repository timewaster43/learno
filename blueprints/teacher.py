from flask import Blueprint, render_template, redirect, request
from exts import db
from models import Student

import app

bp = Blueprint("teacher", __name__, url_prefix="/teacher")


@bp.route('/')
def index():
    if app.isLogin and app.auth == "teacher":
        return render_template("teacher.html")
    else:
        return redirect("/submit/error")


@bp.route('/query')
def query():
    stu_id = request.form.get('id')
    result = Student.query.filter_by(stu_id=stu_id).first()
    voluntary_hour = result.volun_hour
    return voluntary_hour
