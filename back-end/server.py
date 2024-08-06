from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import orders_dao
import uom_doa
import json

connection = get_sql_connection()

app = Flask(__name__)

import product_dao
@app.route('/get_all_products')

def get_all_products():
   products= product_dao.get_all_products(connection)
   response= jsonify(products)
   response.headers.add('Access-Control-Allow-Origin' , '*')
   return response


@app.route('/getUOM' , methods=['GET'])

def get_Uom():
    response= uom_doa.get_uoms(connection)
    response= jsonify(response)
    response.headers.add('Access-Control-Allow-Origin' , '*')
    return response

@app.route('/insertProduct' , methods=['POST'])
def insert_product():
    request_payload= json.loads(request.form['data'])
    product_id= product_dao.insert_new_product(connection, request_payload)
    response= jsonify({
        'order_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin' , '*')
    return response
    
@app.route('/deleteProduct' , methods=['POST'])
def delete_product():
    return_id= product_dao.delete_product(connection, request.form['product_id'])
    response= jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin' , '*')
    return response

@app.route('/insertOrder' , methods=['POST'])
def insert_order():
    request_payload= json.loads(request.form['data'])
    order_id= orders_dao.insert_order(connection, request_payload)
    response= jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin' , '*')
    return response

@app.route('/getAllOrders' , methods=['GET'])
def get_all_orders():
    response= orders_dao.get_all_orders(connection)
    response= jsonify(response)
    response.headers.add('Access-Control-Allow-Origin' , '*')
    return response

if __name__ == "__main__":
    print("Starting pyhton Flask server for Grossery Managment Store")
    app.run(port=5000)


