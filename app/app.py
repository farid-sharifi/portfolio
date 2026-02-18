from flask import Flask
from app.config.config import config,env_name
def create_app():
    from app.routes import home_bp

    app = Flask(__name__)

    app.config.from_object(config.get(env_name,"prod"))
    app.register_blueprint(home_bp)
    
    return app