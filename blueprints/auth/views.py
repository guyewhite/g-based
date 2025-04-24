from flask import url_for, redirect, session
import secrets
from flask_login import login_user, logout_user, login_required
from models import db, User
from authlib.integrations.flask_client import OAuth
from . import auth
import logging

oauth = None

def init_oauth(app):
    global oauth
    oauth = OAuth(app)
    oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        server_metadata_url=(
            'https://accounts.google.com/.well-known/openid-configuration'
        ),
        client_kwargs={'scope': 'openid email profile'}
    )
    return oauth


@auth.route('/login')
def login():
    redirect_uri = url_for('auth.auth_callback', _external=True)
    
    # generate a one-time nonce and remember it in the session
    nonce = secrets.token_urlsafe()
    session['oauth_nonce'] = nonce
    
    # include the nonce in the auth request
    return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)


@auth.route('/auth/callback')
def auth_callback():
    # fetch token
    token = oauth.google.authorize_access_token()

    # retrieve and clear it
    nonce = session.pop('oauth_nonce', None)

    # validate ID token
    userinfo = oauth.google.parse_id_token(token, nonce=nonce)
    
    # Debug logging
    logging.info(f"Received userinfo: {userinfo}")
    
    # look up or create local user
    user = User.query.filter_by(google_id=userinfo['sub']).first()
    if not user:
        user = User(
            google_id=userinfo['sub'],
            google_email=userinfo.get('email'),
            google_name=userinfo.get('name'),
            google_picture=userinfo.get('picture'),
        )
        db.session.add(user)
        db.session.commit()
        logging.info(f"Created new user with picture URL: {user.google_picture}")
    else:
        # Update existing user's information
        user.google_email = userinfo.get('email')
        user.google_name = userinfo.get('name')
        user.google_picture = userinfo.get('picture')
        db.session.commit()
        logging.info(f"Updated user with picture URL: {user.google_picture}")
    
    login_user(user)
    return redirect('/')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/') 