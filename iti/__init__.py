
## initialize application

from flask import Flask
from iti.config import  project_config

def create_app(config_name):
    app = Flask(__name__)
    app_config = project_config[config_name]  # refer to the config class
    # print(app_config)
    # flask you can read required configuration from this object
    app.config.from_object(app_config)


    return app
