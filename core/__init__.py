from flask import Flask, Blueprint


def fCreateFlaskApp():
    flaskApp = Flask(__name__)
    flaskApp.config['SECRET_KEY'] = 'voting_system_3'
    
    from core.views import views
    flaskApp.register_blueprint(views)

    return flaskApp