from flask import Flask
from .src.routers import user

app = Flask(__name__)

@app.route("/", methods=['GET'])

def run_flask_app():
    app.register_blueprint(user.main, url_prefix = '/user')
    app.run()


if __name__ == "__main__":
    run_flask_app()