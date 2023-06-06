
## initialize application

from flask import Flask
from iti.config import  project_config
from iti.models import  db, Student


def create_app(config_name):
    app = Flask(__name__)
    app_config = project_config[config_name]  # refer to the config class
    # print(app_config)

    ### add database configuration ?
    app.config["SQLALCHEMY_DATABASE_URI"]=app_config.SQLALCHEMY_DATABASE_URI
    # app.config["SQLALCHEMY_DATABASE_URI"] = app_config # in this class you will find your desired
    # flask you can read required configuration from this object
    app.config.from_object(app_config)
    db.init_app(app)


    return app
