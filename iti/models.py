

## here you can find the database config
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'students'
    id= db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(200), unique=True, nullable=True)
    accepted = db.Column(db.Boolean, default= True)
    age = db.Column(db.Integer, default=10, nullable=True)


    def __str__(self):
        return self.name

    @classmethod
    def get_all_students(cls):
        return cls.query.all()

    @classmethod
    def get_specific_object(cls, id):
        return  cls.query.get_or_404(id)




