from flask import render_template

from iti.models import Student

# connect to database , and return with students ?
def students_index():
    students = Student.get_all_students()
    return render_template("students/index.html", students =students)


