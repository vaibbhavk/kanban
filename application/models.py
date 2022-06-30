from application.database import db


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)


class List(db.Model):
    __tablename__ = 'lists'
    list_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    cards = db.relationship(
        "Card",
        cascade="all, delete",
        back_populates="list_ref")


class Card(db.Model):
    __tablename__ = 'cards'
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    deadline = db.Column(db.Date, nullable=False)
    completed = db.Column(db.Integer, nullable=False, default=False)
    list = db.Column(db.Integer, db.ForeignKey(
        'lists.list_id', ondelete="CASCADE"), nullable=False)
    list_ref = db.relationship(
        "List",
        back_populates="cards")


class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)


class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)


class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'student.student_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.course_id'), nullable=False)
