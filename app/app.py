from flask import Flask
from flask import jsonify
from flask import request
import time
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "test": "gfhjkm",
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'})


orders = []


@app.route('/')
def index():
    return "Hello, todoAPI!"


@app.route('/statistics', methods=['GET'])
@auth.login_required
def get_orders():
    total = 0
    count = 0
    for order in orders:
        if order['timestamp'] <= time.time() - 60:
            orders.remove(order)
            continue
        total += order['sales_amount']
        count += 1

    try:
        avg = round(total / count, 2)
    except ZeroDivisionError:
        avg = 0

    return jsonify({
        'total_sales_amount': total,
        'average_amount_per_order': avg
    })


@app.route('/sales', methods=['POST'])
@auth.login_required
def add_order():
    if not request or 'sales_amount' not in request.form:
        return '', 400

    try:
        amount = round(float(request.form['sales_amount']), 2)
    except ValueError:
        return '', 400

    order = {
        'sales_amount': amount,
        'timestamp': time.time()
    }
    orders.append(order)
    return '', 202


if __name__ == '__main__':
    app.run(host='0.0.0.0')
