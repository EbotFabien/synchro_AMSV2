from flask import Flask, render_template, url_for,flash,redirect
#from flask_sqlalchemy import SQLAlchemy
#from flask_bootstrap import Bootstrap
##from flask_bcrypt import Bcrypt
#from flask_login import  LoginManager
#from flask_mail import Mail
from app.config import Config
from firebase_admin import credentials, firestore, initialize_app



cred = credentials.Certificate('/Users/pro2015/Desktop/pph folder/synchro/project/app/keys/key_uti.json')
service_user = initialize_app(cred,name='service_users')
db1 = firestore.client(app=service_user)
#bcrypt = Bcrypt()
#login_manager = LoginManager()
#login_manager.login_view ='users.login' #check route 
#login_manager.login_message_category = 'info'
#mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    
    #bcrypt.init_app(app)
    #login_manager.init_app(app)
    #mail.init_app(app)

    from app.entity.users.routes import users
    from app.entity.biblio.routes import biblio
    from app.entity.participants.routes import participants
    app.register_blueprint(users)
    app.register_blueprint(biblio)
    app.register_blueprint(participants)


    return app