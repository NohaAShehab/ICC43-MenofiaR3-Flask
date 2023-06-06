from flask import render_template, redirect, url_for
from iti.models import Student
from iti.students.studentsblueprints import students_blueprint

# connect to database , and return with students ?
### endpoint name must contain (. dot)
## /students
@students_blueprint.route('', endpoint='students_index')
def students_index():
    students = Student.get_all_students()
    return render_template("students/index.html", students =students)


@students_blueprint.route("/<int:id>", endpoint='students_show')
def student_show(id):
    student= Student.get_specific_object(id)
    return render_template("students/show.html", student=student)

@students_blueprint.route('/<int:id>/delete', endpoint='students_delete')
def student_delete(id):
    student= Student.get_specific_object(id)
    student.delete_student()
    url = url_for('iti.students_index')
    return redirect(url)
