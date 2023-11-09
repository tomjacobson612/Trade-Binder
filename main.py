from flask import Flask, render_template, request, jsonify, redirect, url_for
from pokemontcgsdk import Card
from dbmodel import model

app = Flask(__name__)
model = model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardsearch.html')
def card_search():
    return render_template('cardsearch.html')

@app.route('/collection.html')
def collection():
    data = model.select()
    return render_template('collection.html', data=data)

@app.route('/search', methods=['POST'])
def search():
    cards = Card.where(q='name:'+ request.form['search_query'])
    if cards:
        return render_template('cardsearch.html', cards=cards, search_query=request.form['search_query'])
    else:
        return redirect('cardsearch.html')
    
@app.route('/add', methods=['POST'])
def add():
    model.insert(request.form['name'], request.form['num'], request.form['img'])
    return redirect(url_for('collection'))

if __name__ == "__main__":
    app.run(debug=True)