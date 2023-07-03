from flask import Blueprint, render_template, request, redirect
import exts
from models import Teacher, Student
from exts import db
import app

bp = Blueprint("account", __name__, url_prefix="/account")


@bp.route('/register')
def register():
    return render_template('add.html')


@bp.route('/add', methods=['POST'])
def add_user():
    new_id = request.form.get('new-id')
    new_name = request.form.get('new-name')
    new_password = request.form.get('new-password')
    new_auth = request.form.get('new-auth')
    new_password = exts.encrypt(new_password)
    print(new_password)
    if new_auth == "teacher":
        user = Teacher(name=new_name, password=new_password)
    else:
        user = Student(stu_id=new_id, volun_hour=0, name=new_name, password=new_password)
    # 将定义的对象加到session
    db.session.add(user)
    # 讲session同步到数据库
    db.session.commit()
    return render_template('add_success.html')


@bp.route('/edit', methods=['POST'])
def edit_password():
    new_psw = request.form.get('newpsw')
    new_psw = exts.encrypt(new_psw)
    users = Teacher.query.filter_by(name=app.name).first()
    users.password = new_psw
    db.session.commit()


@bp.route('/delete')
def delete_user():
    if app.isLogin:
        user = Teacher.query.filter_by(name=app.name).first()
        db.session.delete(user)
        db.session.commit()
        app.name = ""
        app.isLogin = False
        return "删除成功"
    else:
        return redirect('/submit/error')


@bp.route('/index')
def account_index():
    if app.isLogin:
        destination = "/" + app.auth
        return redirect(destination)
    else:
        return redirect('/submit/error')
