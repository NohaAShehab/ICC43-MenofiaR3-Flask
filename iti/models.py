

## here you can find the database config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import url_for
db= SQLAlchemy()


class Department(db.Model):
    __tablemodel__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self):
        return self.name

    @classmethod
    def get_all_departments(cls):
        return cls.query.all()





class Student(db.Model):
    __tablename__ = 'students'
    id= db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(200), unique=True, nullable=True)
    accepted = db.Column(db.Boolean, default= True)
    age = db.Column(db.Integer, default=10, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.now,onupdate=datetime.now, nullable=True)
    dept_id = db.Column(db.Integer,
                        db.ForeignKey("department.id"), nullable=True)


    def __str__(self):
        return self.name

    @classmethod
    def get_all_students(cls):
        return cls.query.all()

    @classmethod
    def get_specific_object(cls, id):
        return  cls.query.get_or_404(id)

    def delete_student(self):
        db.session.delete(self)
        db.session.commit()
        return True


    def get_show_url(self):
        return url_for("iti.students_show", id=self.id)

    @property
    def get_delete_url(self):
        return url_for("iti.students_delete", id=self.id)






