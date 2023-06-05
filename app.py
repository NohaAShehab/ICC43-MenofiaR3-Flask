# import Flask ?

from flask import Flask
from flask import request
from flask import  render_template


# ### create your first app
app = Flask(__name__)  ## __name__  ==> python assign this variable with module name


# when you check it --> from the module itself? ---> output __main__

# ################## define first url in your application #####################
# ## no need to add request object
@app.route('/')
def helloworld():
    # no need to return with http response ---> return with it automatically
    return "<h1 style='color:red; text-align:center'>Nice to see you here in flask </h1>";


###################### check request ?
@app.route('/request')
def request_info():
    print(f"Request here ---> {request}")
    return "<h1 style='color:purple; text-align:center'>Welcome to Request page </h1>";


# #################### add url / route to my application

def test_new_url():
    list_of_courses = ["python", "django", "flask", "odoo", "postgres"]
    return list_of_courses


# ############# register routes/url to the application
app.add_url_rule("/test-url",view_func=test_new_url)

# ############## part of url --> changeable
@app.route("/sayhello/<name>")
def sayhello(name):
    return f"<h1 style='color:green'> Hello {name} </h1>";


## customize page 404 not found
@app.errorhandler(404)
def page_not_found(error):  # you must pass the error object to the function
    return  f"<h1 style='color:red'> Sorry the request page not found on the server  </h1>";


@app.route("/testerror")
def test_error():
    # print(name)
    return "Page found"


# ####################################### jinja template
students = [{"id":1, "name":"Ahmed", "track":"Python"},
            {"id":2, "name":"Noha", "track":"AI"},
            {"id":3, "name":"Mostafa", "track":"cloud"}]

@app.route("/students")
def students_index():
    ##
    # return students
    ## send students to the template
    return  render_template("students/index.html", students=students)


# default of end_point ---> function name
@app.route("/students/<int:id>", endpoint='students.show')
def get_student(id):
    print(type(id))
    returned_student = filter(lambda std:std['id']==id, students)
    returned_student=  list(returned_student)
    if returned_student:
        # print(returned_student[0])
        # return returned_student[0]
        student= returned_student[0]
        return render_template("students/show.html", student=student)
    # return "not found", 404
    return render_template("pagenotfound.html"), 404





# ## limit =-> code in this module should run here only
if __name__ == '__main__':
    print(f" this is my module {__name__}")
    ### start flask app
    app.run(debug=True)
