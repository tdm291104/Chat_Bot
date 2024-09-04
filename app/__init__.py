from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import the Blueprint
    from .routes import bp

    # Register the Blueprint
    app.register_blueprint(bp)

    return app