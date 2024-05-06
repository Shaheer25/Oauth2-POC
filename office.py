from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import oauth
from flask import request
import base64
import requests
from urllib.parse import urlparse, parse_qs
from flask import jsonify
import psycopg2

# conn = psycopg2.connect(user="testuser", password="examplepass", host="localhost", port="5432")
# print(conn.encoding)
# print("Database Connected....")
# token_endpoint = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
# client_id = "412ddd5e-f8d8-47a4-82de-c2934d1339b4"
# client_secret = "lZz8Q~_KXs4CqGlhTSJrlu7Gm-ZgdQ9PO4kNYchW"
# redirect_uri = "https://google.com"
# code = 'M.C518_BAY.2.U.2feabbe5-839b-62be-7244-cc223a63d0ca'
# scope = "Calendars.Read"

# data = {
#     "client_id": client_id,
#     "client_secret": client_secret,
#     "redirect_uri": redirect_uri,
#     "code": code,
#     "grant_type": "authorization_code",
#     "scope": scope
# }

# response = requests.post(token_endpoint, data=data)
# print(response.json())

# if response.status_code == 200:
#     token_response = response.json()
#     access_token = token_response.get("access_token")
#     print("Access token:", access_token)
# else:
#     print("Token request failed:", response.text)

####__________GET CALENDAR INFO _______________________


# graph_endpoint = 'https://graph.microsoft.com/v1.0/me/calendar/events'

# # # token = response.json()
# bearer = 'EwBoA8l6BAAUbDba3x2OMJElkF7gJ4z/VbCPEz0AARkxJ5+/MaU37KlDioL81A5MWj6IOnPK2up7sHashdX7c7ZO5xDH5Id8d6M4bCd7VlWXlWFd4Res301wQ6h1yBkDfg7PQ+28gQMWR84s4abChZ30giUEULmGrxM7UQ6Oa0XIpNLNGRup8q9VSeFzh+5FSyjTZ4DzhDQOS7KPQD9wetCcGMG17UHDyxVm6bE4EYD7Is4OX8AJ834nekiVou92pFH+Jl7xDCAYCAtE9WZiCDVZqZAezw5hKjOTQPs6kN95WpszGEQHe63MMbSmyZ1YNAwmRWpT9H8Bj8F3H62gBVPURcSZDIF7tST5FwXeFnHP0OdgzlwStjNc3iUq5wEDZgAACB1td5GhYc29OAIfDWN7hpTFYJfjTMEQy1gfpce8Lzn2nbxp5mjBCWKggL0Sb31bK+njLjv6QIheT/fXLAH0wtwkX+v83rAK8Ij2uPBw8hTVxvKZjxVAui6GoLS+HJqBfQRwW32fbGgFhjDdP+H2b+z9zRHesZgJmgzhgJkOJuiGu3zIR8IOvDNXaSnuWxUSpNYL4Lhf6zvf9Q5ZV/WIOtyuDrzHEG18bljL5JGV+5tn/zgLPc+LYL9UQhYWcrkJycGv2NHG6Msk2adt2elZ2GI5H0EoQQVHJbm+Y9802gwquuFP9xOBfy129XxkUmYgGKibp/IWxX0v6pFpqY4SME4xPz58JQBUXva8xSP6Lmp+C7+NNMBCDzfpa7aAeKFp/aja3VGfurR9FPoBC/HnUW4H8RKw9yt1E+pqB6hd/D6fk6EHvWkIYn4uvQ0Lh+PW8Am51rU1P3EV9lpUjiW31jYlTSuBv4kn0/tOJhrjb8Q/hChmkXsvN57nB9YQQ+BqhxqeQQFfIWriNN5wPLzKzuPsvdF8lySCCNaM/QaRKwz9T7O8OTY/bNnuTnd8S68xfTzNUP0NG+sLICk5aeeMHBTcs+FLaRltXaLmO+7WjI5vY53URPzB30PXUOtEAGB6v6uPJei2RT0soh8yX1JSq006vHoozJ6Xuc4VgM5HcTUiQ1Xk/O97RdlqtRgvzLZBIAMfhwgNek3M/dOxTOgsC18vL5YjxpmL19PfcFGzcSpQwmEN2MejgB53CLiPg5rQj1I/fAI='

# headers = {
#     'Authorization': f'Bearer {bearer}'
# }
# response = requests.get(graph_endpoint, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse and print the calendar events
#     events = response.json().get('value', [])
#     for event in events:
#         print(event['start'])
#         print(event['end'])
# else:
#     print('Failed to retrieve calendar events:', response.text)

from flask import Flask, request, redirect, session
from requests_oauthlib import OAuth2Session
import os
token_endpoint = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
client_id = "412ddd5e-f8d8-47a4-82de-c2934d1339b4"
client_secret = "lZz8Q~_KXs4CqGlhTSJrlu7Gm-ZgdQ9PO4kNYchW"
redirect_uri = "https://google.com"
scope = "Calendars.Read openid offline_access User.Read email profile"
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Define OAuth2 parameters
authorization_base_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
# scope = ['Calendars.Read']

# Initialize OAuth2 session
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
def callback():
    # Verify state parameter
    tenant_id = 'f8cdef31-a31e-4b4a-93e4-5f571e91255a'
    token_endpoint = f"https://login.microsoftonline.com/consumers/oauth2/v2.0/token"
    client_id = "412ddd5e-f8d8-47a4-82de-c2934d1339b4"
    client_secret = "lZz8Q~_KXs4CqGlhTSJrlu7Gm-ZgdQ9PO4kNYchW"
    redirect_uri = "https://google.com"
    scope = "Calendars.Read, offline_access, User.Read,openid, email, profile"
    # response_state = request.args.get('state')
    # if response_state != session.pop('state', None):
    #     return "CSRF Warning! State mismatch."
    
    # Exchange authorization code for access token
    authorization_response = 'https://www.google.com/?code=M.C518_BAY.2.U.c026fa29-8869-34ff-06b0-4705021e3e0d&state=JlKqGkTTCMlGtbwHALw4NQ%3D%3D'
    # token = oauth.fetch_token(token_url, authorization_response=authorization_response, client_secret=client_secret, scope=scope)
    
    # # Access token is now available in token['access_token']
    # return "Access Token: {}".format(token['access_token'])

    parsed_url = urlparse(authorization_response)

    query_params = parse_qs(parsed_url.query)

    code = query_params.get('code')[0]

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
    
@app.route('/refresh_token')
def refresh_token():
    # Define OAuth2 parameters
    token_endpoint = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    client_id = "412ddd5e-f8d8-47a4-82de-c2934d1339b4"
    client_secret = "lZz8Q~_KXs4CqGlhTSJrlu7Gm-ZgdQ9PO4kNYchW"
    redirect_uri = "https://google.com"
    scope = "Calendars.Read"

    # Retrieve the refresh token (for example, from a database)
    refresh_token = "M.C518_BAY.0.U.-CrW*W3EWdBwZwzg0Ngff467wv3npiSiGbFsXBuuud7whX!ZkrofcXR9k3qgvLG*0*2GZMQt2y!h20xS2z2SO7lREmYOjhvNw2Xj1oLaO6uA7uNI5PeNEa0wWpvYjrveRfiaMbr72!rpOYIGz6lc!tIqyRDdKxApXPwNQMowRPdY8WE1OLp55pE10hE5LJZBUodjiYKjfpfKNDnwC6DjujPc04YkZw6uWIbK4ie63JbFtNlAJ*KOz6AYVl54CBiwIcCI!NvPjKZ3wrV!YowpA8fVJ9PIEtfbC0bApBeqfeZsDHye5eWAEhTs5sTp09PX*quPnKCcEvvc2*UxOFkk0vSwLJ!a1RAlq5RHnkba5joDFKBUSaBanhRmQtVeYmsbRT6tZwqqJXxeFGG7iuEZjd3A$"

    # Prepare data for refreshing the token
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
        "scope": scope
    }

    # Send a POST request to the token endpoint to refresh the token
    response = requests.post(token_endpoint, data=data)

    if response.status_code == 200:
        # Parse the token response
        token_response = response.json()
        access_token = token_response.get("access_token")

        # Update the refresh token in the database with the new one
        # if new_refresh_token:
        #     update_refresh_token_in_database(new_refresh_token)

        print(token_response)

        print("Access token:", access_token)

        return f"Access Token: {access_token}"
    else:
        print("Token refresh failed:", response.text)
        return "Failed to refresh token"
    
@app.route('/calendars')
def calendars():
    try:
        graph_endpoint = 'https://graph.microsoft.com/v1.0/me/calendar/events'
        user_endpint = 'https://graph.microsoft.com/v1.0/me'

        bearer = "EwBwA8l6BAAUbDba3x2OMJElkF7gJ4z/VbCPEz0AAS8VwYz7DPrH3smPa4aRit1KYjhJ+1qvRv8mEcDfd5QLS4E24agbveH/Z0nSdUCGKnGgGzN1dymtQF1U5zNI/acGTb8WnzPU38nQmPIbOJp/4NC0OZmtn2m4ng4s5to5ykHIBDJPoqqZWkxl4pCtT5LST6++Rg/Z8EnXfModEOXE3yH0nY8NDUJx41RL/+uEJDAYHqCSQjfrfqgO8vphR+FLsB5txLNJuoGQ0B4JILOKC5mcp02cK9zj3obetHPGKLGGEBkz8JUqFjzrG8ilo7RbU+fk63Lat6ii3STmFdevdlxMvZvP+486jnhGOUfuQMj69MEruXD6sFmj4KACoI0DZgAACJFKCDxltq/7QAK9FSnEufQEcDCKRTsoLv+DrfJ6awiU9WU8yYcLjybMxZw5ssFgzbBt7W+3tXTQuPDPQBieyOs9Z4TPU+CIjoqRyKDvOrmMnE3st9u2LqrvB+9nBuV0gjEgn9eoc8oxZ8NWtXjF+0uB25S4DG3dJm6qulktIHd4iSMFlUHR16Y2TRYwww5kjBDZgCHiib5/PmKlt24S8lt0EN9quAqQpuv3eKTqv8gb+WNfyl7503Oc0IQOAvWz+Qal9dV4m9S6lh48Mcf6DjxhZYp6SmMD3IlJiDScLGAAyrKNEo5iULGvUjGfwPgPwIIinJvUj0wTlEIDLjBo2QhGuTrbf8weUNn/JyINcOmdawS4Ut0w6UtYyRGxZb5EM/MTsMqIq8eEdHkYVu4ZjHZ49uEaQbCiAsgB2ZyqaGR5HgmYVLL8ttRUWGMeiZIwTi96Rmc3SNtqBBCdfulkXMarCGuSvCfEm+FMyOeFYE339Pj7yUAGhXuaeob/6kvglXhyPRffEqEFdA9PIkMTDlkdgfsAmWyhZGDUjfdvEAyGZQJ2uFpFyqWUBh9QzEZEOCwViuf/q3hByEOB88uLAy4UlOk+DGcDl9s5EJ3wpkRuEpeAH/qfs6z7yL4/J9jXQIsat4XdaBPzfC+IhHD2i6AkLu0582pS9z7GyCDgMySBgDW8YWLRopIp6t22t1LnZUb9kXcpQFRltCpNfMFszVjuaSP4Qof8cm9x+6fbjdgAZz3nN9DZiUpEvZVw9v77UiXrEdXGr824NsuIAg=="

        headers = {
            'Authorization': f'Bearer {bearer}'
        }
        response = requests.get(graph_endpoint, headers=headers)
        resp = []
        user_response = requests.get(user_endpint, headers=headers)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse and print the calendar events
            events = response.json().get('value', [])
            for event in events:
                print(event['start'])
                print(event['end'])
                dumps = {
                    "start":event['start'],
                    "end":event['end']
                }
                resp.append(dumps)
        else:
            print('Failed to retrieve calendar events:', response.text)

        user_data = None
        print(user_response.json())
        if user_response.status_code == 200:
            user_data = user_response.json()
            print(user_data)

        return f"data {resp} , user {user_data}"

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(port=3000)  # Enable HTTPS for local development