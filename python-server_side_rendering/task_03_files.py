from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_data():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        return []

def load_csv_data():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            return [dict(id=int(row['id']), name=row['name'], category=row['category'], price=float(row['price'])) for row in reader]
    except Exception as e:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    id_filter = request.args.get('id')
    data = []
    error = None

    if source == 'json':
        data = load_json_data()
    elif source == 'csv':
        data = load_csv_data()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Filter by ID if provided
    if id_filter:
        try:
            id_int = int(id_filter)
            data = [item for item in data if item['id'] == id_int]
            if not data:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID format"
            data = []

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
