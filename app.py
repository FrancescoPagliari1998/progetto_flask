from flask import Flask, render_template
import csv

app = Flask(__name__)



@app.route('/')
def home():
    bottoni = {
        'b1': 'film',
        'b2': 'music',
        'b3': 'book',
    }
    return render_template('home.html', titolo='MediApp'.upper(), bottoni=bottoni)

@app.route('/book')
def book():
    books = [ { "author": "Yuval Noah Harari", "title": "Sapiens: A Brief History of Humankind", "year": 2011 }, { "author": "Tara Westover", "title": "Educated: A Memoir", "year": 2018 }, { "author": "Cormac McCarthy", "title": "The Road", "year": 2006 } ]
    return render_template('book.html', books=books)



if __name__ == '__main__':
    app.run(debug=True)