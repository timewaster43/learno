from exts import db


class Teacher(db.Model):
    __tablename__ = "teacher"
    name = db.Column(db.String(10), primary_key=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)


class Student(db.Model):
    __tablename__ = "student"
    stu_id = db.Column(db.Integer, primary_key=True,  nullable=False)
    volun_hour = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(64), nullable=False)
