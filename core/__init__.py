from flask import Flask, Blueprint


def fCreateFlaskApp():
    flaskApp = Flask(__name__)
    
    from core.views import views
    flaskApp.register_blueprint(views)

    return flaskApp