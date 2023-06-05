# import Flask ?

from flask import Flask
from flask import request, redirect, url_for
from flask import  render_template
from flask_sqlalchemy import SQLAlchemy


# ### create your first app
app = Flask(__name__)  ## __name__  ==> python assign this variable with module name

#### connect to database
# tell the application the database path you need

## http://www.ggogle.com/mm
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)  # you are now connected sqlite
# instance folder---> contain database --->

###########################################################
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


#################### Model Section ##################
class Product(db.Model):
    __tablename__= 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer)

# to apply model content to the database
# go to flask shell
# db.create_all() =-->


# ############ routes for crud on products
@app.route("/products", endpoint='products.index')
def get_all_products():
    products = Product.query.all()
    return render_template("products/index.html", products=products)


@app.route("/products/<int:id>", endpoint="products.show")
def get_product(id):
    product = Product.query.get_or_404(id)
    return render_template("products/show.html", product = product)


@app.route("/products/<int:id>/delete", endpoint="products.delete")
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    url  = url_for('products.index')
    return redirect(url)

    # product = db.get_or_404(Product, id)
    # db.session.delete(product)
    # db.session.commit()
    # return redirect(url_for("products.index"))


@app.route("/products/create", methods = ["GET", "POST"],endpoint="products.create")
def create_product():
    ## request method POST
    if request.method=="POST":
        print(request.form)
        product_name= request.form["name"]
        product_price = request.form["price"]
        product = Product(name=product_name, price=product_price)
        db.session.add(product)
        db.session.commit()

        return redirect(url_for('products.index'))

    ## request method GET ?
    return render_template("products/create.html")



# ## limit =-> code in this module should run here only
if __name__ == '__main__':
    print(f" this is my module {__name__}")
    ### start flask app
    app.run(debug=True)
