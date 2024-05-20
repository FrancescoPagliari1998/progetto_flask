from flask import Flask, render_template
import csv
import mysql.connector


app = Flask(__name__)
app.config.from_object('config.Config')

def create_db_connection():
    db_config = {
        'host': app.config['MYSQL_HOST'],
        'user': app.config['MYSQL_USER'],
        'password': app.config['MYSQL_PASSWORD'],
        'database': app.config['MYSQL_DB']
    }
    return mysql.connector.connect(**db_config)

def execute_query(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


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
    books = execute_query('SELECT * FROM book')
    return render_template('book.html', books=books)

@app.route('/api/book')
def api_book():
    books = execute_query('SELECT * FROM book')
    return books



if __name__ == '__main__':
    app.run(debug=True)