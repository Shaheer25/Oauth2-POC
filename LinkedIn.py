from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import oauth
from flask import request
import base64
import requests
from urllib.parse import urlparse, parse_qs
from flask import jsonify
import psycopg2

from flask import Flask, request, redirect, session
from requests_oauthlib import OAuth2Session
import os

app = Flask(__name__)
app.secret_key = 'Muhammad Shaheer'

client_id = "86ly1dewra732h"
redirect_uri = 'http://127.0.0.1:5555/callback'
scope='w_member_social'
authorization_base_url = 'https://www.linkedin.com/oauth/v2/authorization'

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

@app.route('/')
def index():
    # Generate state parameter and store it in the session
    state = base64.urlsafe_b64encode(os.urandom(16)).decode('utf-8')
    session['state'] = state
    
    # Redirect user to Azure AD login page with state parameter
    authorization_url, _ = oauth.authorization_url(authorization_base_url, state=state)
    return redirect(authorization_url)



@app.route('/callback')
def callaback():
    token_endpoint = f"https://www.linkedin.com/oauth/v2/accessToken"
    client_id = "86ly1dewra732h"
    client_secret = "teDa0UDrwbXobF0a"
    redirect_uri = 'http://127.0.0.1:5555/callback'
    scope='w_member_social'
    response_state = request.args.get('state')
    if response_state != session.pop('state', None):
        return "CSRF Warning! State mismatch."


    code = response_state = request.args.get('code')

    print(code)

    data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "code": str(code),
    "grant_type": "authorization_code",
    "scope": scope
    }

    response = requests.post(token_endpoint, data=data)
    print(response.json())

    if response.status_code == 200:
        token_response = response.json()
        access_token = token_response.get("access_token")
        refresh_token = token_response.get("refresh_token")
        print("Access token:", access_token)
        print("Refresh token:", refresh_token)
        return f"Access Token: {access_token}"
    else:
        print("Token request failed:", response.text)
        return f"Failed"

if __name__ == '__main__':
    app.run(port=5555) 