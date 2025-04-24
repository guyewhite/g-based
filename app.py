# g-based
# A template for Google-authenticated flask applications.
# by Guy E. White
# Offered under MIT license

# includes
from flask import Flask
from flask_login import LoginManager
import os
from models import db, User
from blueprints.auth import auth
from blueprints.auth.views import init_oauth
from blueprints.dashboard import dashboard

# database setup
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'mysql+pymysql://user:pass@localhost:3306/mydb'
)

app.config['GOOGLE_CLIENT_ID'] = os.getenv('GOOGLE_CLIENT_ID')
app.config['GOOGLE_CLIENT_SECRET'] = os.getenv('GOOGLE_CLIENT_SECRET')

db.init_app(app)

app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Flask-Login setup
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

# manage session cookie and database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialize OAuth
init_oauth(app)

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(dashboard)

