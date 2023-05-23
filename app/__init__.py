from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.errorhandler(404)
    def error404(error):
        return render_template('error404.html')
    return app
