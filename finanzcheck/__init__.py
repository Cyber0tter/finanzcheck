import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create an configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'finanzcheck.sqlite'),)

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page
    @app.route("/")
    def home():
        return render_template('index.html')
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
