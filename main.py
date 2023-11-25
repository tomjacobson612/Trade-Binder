from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from pokemontcgsdk import Card
from dbmodel import model
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
model = model()
app.secret_key = env.get("APP_SECRET_KEY")

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

@app.route("/")
def home():
    return render_template("index.html", session=session.get('user'))

@app.route('/cardsearch.html')
def card_search():
    return render_template('cardsearch.html')

@app.route('/collection.html')
def collection():
    email = session.get('user').get('userinfo').get('email')
    data = model.select(email)
    return render_template('collection.html', data=data, email=email)

@app.route('/add.html')
def add():
    return render_template('add.html')

@app.route('/search', methods=['POST'])
def search():
    cards = Card.where(q='name:'+ request.form['search_query'])
    if cards:
        return render_template('cardsearch.html', cards=cards, search_query=request.form['search_query'])
    else:
        return redirect('cardsearch.html')
    
@app.route('/add', methods=['POST'])
def add_card():
    name = request.form['add_name']
    id = request.form['add_id']
    img_url = request.form['add_img_url']
    email = session.get('user').get('userinfo').get('email')

    if name == "" or id == "" or img_url == "":
        return redirect(url_for('collection'))
    else:
        model.insert(email, name, id, img_url)
        return redirect(url_for('collection'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))