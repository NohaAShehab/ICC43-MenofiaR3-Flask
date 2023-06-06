



#### configuration application development server
## debug
## dburl

##### config ---> production


class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= "sqlite:///db.sqlite"


class ProductionConfig(Config):
    DEBUG=False
    ## path postgres ?
    # postgresql://username:password@localhost:portnumber/databasename
    SQLALCHEMY_DATABASE_URI= "postgresql://pymenofia43:iti@localhost:5432/pymenofia43"


project_config= {
    "dev": DevelopmentConfig,
    "prd":ProductionConfig
}




