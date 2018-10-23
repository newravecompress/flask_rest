from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
import time

app = Flask(__name__)

orders = []


@app.route('/')
def index():
    return "Hello, todoAPI!"


@app.route('/statistics', methods=['GET'])
def get_orders():
    for order in orders:
        if order['timestamp'] <= time.time() - 60:
            orders.remove(order)
    # orders = [o for o in orders if o['timestamp'] > time.time() - 60]
    # orders = list(filter(lambda o: o['timestamp'] > time.time(), orders))
    count = len(orders)
    total = sum(o['sum'] for o in orders if o['timestamp'] > time.time() - 60)
    return jsonify({'total': total, 'avg': total/count})


@app.route('/sales', methods=['POST'])
def add_order():
    if not request or 'sum' not in request.form:
        abort(400)
    order = {
        'sum': int(request.form['sum']),
        'timestamp': time.time()
    }
    orders.append(order)
    return jsonify({'order': order}), 202


if __name__ == '__main__':
    app.run(debug=True)

# curl -i http://localhost:5000/statistics
# curl -i -H "Content-Type: application/json" -X POST -d '{"sum":111111}' http://localhost:5000/sales
