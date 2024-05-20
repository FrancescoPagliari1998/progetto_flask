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





if __name__ == '__main__':
    app.run(debug=True)