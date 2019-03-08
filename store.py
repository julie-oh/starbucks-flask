from flask import Flask, url_for, request
from partner import Partner

app = Flask(__name__)

manager = Partner()


@app.route('/')
def index():
    return 'Welcome, Starbucks! :) '


@app.route('/get_order', methods=['POST'])
def get_order():
    order_info = request.get_json()

    ordered_menu = manager.take_order(order_info)

    # return str(ordered_menu)
    return 'total_price: {}, total_time: {}'.format(ordered_menu['price'], ordered_menu['time'])

