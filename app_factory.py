from flask import Flask, jsonify, request
from models import User, db
import utils
from flask_mail import Mail


def create_app(cfg_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(cfg_filename)
    db.init_app(app)
    mail_server = Mail(app)

    # Define routes (TODO:Change to blueprint this routes)
    @app.route("/user", methods=["POST"])
    def user():
        name = request.args["name"]
        email = request.args["email"]
        try:
            utils.send_deferred_email(app, mail_server, name, email)
            user = User(name, email)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return jsonify({"error": f"500 Unexpected error:{e}"}), 500
        return jsonify({"User": name}), 200

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "404 Not Found"}), 404

    return app, mail_server
