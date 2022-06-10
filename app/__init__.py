from flask import Flask
from config import Config
from .auth.routes import auth
from .api.routes import api
from flask_cors import CORS

from .models import db, login
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

app.register_blueprint(auth)
app.register_blueprint(api)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to see this page.'
login.login_message_category = 'danger'

from . import routes