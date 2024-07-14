from flask import render_template

# Optionally use a Blueprint
# main = Blueprint('main', __name__)


def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    # Register blueprint if using
    # app.register_blueprint(main)
