import requests
from flask import Flask, render_template, request, jsonify, redirect, url_for
from pokemontcgsdk import Card

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardsearch.html')
def card_search():
    return render_template('cardsearch.html')

@app.route('/search', methods=['POST'])
def search():
    cards = Card.where(q='name:'+ request.form['search_query'])
    if cards:
        return render_template('cardsearch.html', cards=cards, search_query=request.form['search_query'])
    else:
        return redirect('cardsearch.html')

if __name__ == "__main__":
    app.run(debug=True)