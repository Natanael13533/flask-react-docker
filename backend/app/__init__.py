from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config
from app.models import db
from app.routes import api
from flask_jwt_extended import JWTManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
CORS(app)  # supaya React bisa mengakses API
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)