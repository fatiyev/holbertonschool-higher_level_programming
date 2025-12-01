from flask import Flask, render_template, request
import sqlite3
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    filename = "./data/items.json"
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            items = json.loads(f.read())["items"]
    except (FileNotFoundError, KeyError):
        items = []
    return render_template('items.html', items=items)


@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')
    items = []
    message = None

    if source in ['json', 'csv']:
        filename = f"./data/products.{source}"
        with open(filename, 'r', encoding="utf-8") as f:
            if source == 'json':
                items = json.loads(f.read())
            else:
                dictionaries = csv.DictReader(f)
                for item in dictionaries:
                    items.append(item)
    elif source == "sql":
        filename = "./data/products.db"
        connection = sqlite3.connect(filename)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, name, category, price
            FROM Products
        """)
        result = cursor.fetchall()
        connection.close()
        items = [dict(row) for row in result]
    else:
        message = "Wrong source"

    if id and not message:
        id = int(id)
        valid = [item["id"] for item in items]
        if id not in valid:
            message = "Product not found"

    return render_template('product_display.html', items=items, id=id, message=message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)