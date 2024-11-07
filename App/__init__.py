from flask import Flask

def create_app():
    app = Flask(__name__)
    with app.app_context():
        from . import routes  # Import routes to register them with the app
    return app