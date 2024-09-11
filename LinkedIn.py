from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import oauth
from flask import request
import base64
import requests
from urllib.parse import urlparse, parse_qs
from flask import jsonify
import asyncio

from flask import Flask, request, redirect, session
from requests_oauthlib import OAuth2Session
import os

app = Flask(__name__)
app.secret_key = 'Muhammad Shaheer'

client_id = "86ly1dewra732h"
redirect_uri = 'http://127.0.0.1:5555/callback'
scope='profile,email,openid'
authorization_base_url = 'https://www.linkedin.com/oauth/v2/authorization'

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

@app.route('/')
def index():
    try:
        state = base64.urlsafe_b64encode(os.urandom(16)).decode('utf-8')
        session['state'] = state
        # authorization_url, _ = oauth.authorization_url(authorization_base_url, state=state)
        data = {
            "client_id": client_id,
            "state": state,
            "redirect_uri": redirect_uri,
            "response_type": "code",
            "scope": scope
        }
        authorization_url, _ = requests.post(
            authorization_base_url , data=data
        )
        print(authorization_url)
        return redirect(authorization_url)
    except Exception as e:
        print(str(e))



@app.route('/callback')
def callaback():
    token_endpoint = f"https://www.linkedin.com/oauth/v2/accessToken"
    client_id = "86ly1dewra732h"
    client_secret = "teDa0UDrwbXobF0a"
    redirect_uri = 'http://127.0.0.1:5555/callback'
    scope='profile,email,openid'
    response_state = request.args.get('state')
    # if response_state != session.pop('state', None):
    #     return "CSRF Warning! State mismatch."


    code = response_state = request.args.get('code')

    print(code)

    data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "code": str(code),
    "grant_type": "code",
    "scope": scope
    }

    response = requests.post(token_endpoint, data=data)
    print(response.json())

    if response.status_code == 200:
        token_response = response.json()
        access_token = token_response.get("access_token")
        refresh_token = token_response.get("refresh_token")

        return f"Access Token: {access_token}"
    else:
        print("Token request failed:", response.text)
        return f"Failed"
    
@app.route('/get-posts')
def getPosts():
    try:
        token = 'AQWrAqAUElYsrjEoAxJjaOvcC3fpth_kVoP1TZPygF-PVWjsmQAni-TH53FTwhVXOL2-Sn_PmTLWcboPRaQOk-SE1TUhFbcmo6KNLF3Ne9s-iNQiK7y9Lbmw_3RLaYg7GysGAkKKr9VMBL4LPiNx0Y8C6ALaQFsZAFiAZKMKoMh_ywQKgImsnsd0KOsfspACGqII5nNTKprL3vTRy8kCPiV88e3kQUarjizD8tjdLfQHEbh4ETDIs5Bb03y0xbiDDIAPseL48kK19FFleikmyCXp640fADFwvhWCAVYxrMACuh1qjv8wd-0Rqbxtvay7fN8D5YoQxid1vy0hx9YPx9_Q1Eb8Cw'
        urn = 'https://www.linkedin.com/in/shaheer-67332b243/'
        API_URL = f"https://api.linkedin.com/v2/shares?q=owners&owners={urn}&sortBy=LAST_MODIFIED&sharesPerOwner=100"
        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(url=API_URL, headers=headers)
        print(response.json())
        if response.status_code == 200:
            print(response.json())

            return jsonify(response)
    except Exception as ex:
        return str(ex)


if __name__ == '__main__':
    asyncio.get_event_loop()
    app.run(port=5555) 