from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

from os import  path
#db=SQLAlchemy()
#database_name="database.db"
def create_app():
    app=Flask(__name__)

    app.config['SECRET_KEY']='ninad'
  #  app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{database_name}'
 #   db.init_app(app)
    from .views import views
    from .Register import Register
    # bcrypt = Bcrypt(app=app)
    app.register_blueprint(Register, url_prefix='/')
    app.register_blueprint(views,url_prefix='/')
    #app.register_blueprint(Login, url_prefix='/')

    #from .model import User,LoginInfo
#    create_database(app)
    return app
# def create_database(app):
#     if not path.exists('website/'+database_name):
#         db.create_all(app=app)
#         print('Created Database')
