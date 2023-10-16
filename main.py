from flask import Flask, render_template
from pokemontcgsdk import Card

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardsearch.html')
def card_search():
    return render_template('cardsearch.html')

if __name__ == "__main__":
    app.run(debug=True)