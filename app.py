from flask import Flask, render_template, redirect
from models import Teacher, Student
from exts import db
import config
from blueprints.account import bp as account_bp
from blueprints.login import bp as login_bp
from blueprints.submit import bp as submit_bp
from blueprints.student import bp as student_bp
from blueprints.teacher import bp as teacher_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)
# ORM模型映射三步
# 1. flask db init: 这个只用运行一次
# 2. flask db migrate
# 3. flask db upgrade


app.register_blueprint(account_bp)
app.register_blueprint(login_bp)
app.register_blueprint(submit_bp)
app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)

isLogin = False
auth = ''
name = ''


teacher_class = Teacher()
student_class = Student()

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    global isLogin
    isLogin = False
    return render_template('index.html')


@app.route('/logout')
def logout():
    global isLogin
    isLogin = False
    return redirect("/")


@app.route('/edit', methods=['GET', 'POST'])
def edit_user():
    if isLogin:
        users = Teacher.query.filter_by(name=name).first()
        print(users.password)
        # users.password = "benjamin"
        # db.session.commit()
        return render_template("edit.html", psw=users.password)
    else:
        return redirect("/submit/error")


if __name__ == '__main__':
    app.run()
