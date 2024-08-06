from sql_connection import get_sql_connection
from datetime import datetime

def check_product_exists(cursor, product_id):
    cursor.execute("SELECT COUNT(*) FROM products WHERE product_id = %s", (product_id,))
    result = cursor.fetchone()
    return result[0] > 0

def insert_order(connection, order):
    try:
        cursor = connection.cursor()

       
        order_query = ("INSERT INTO `order` "
                       "(customer_name, total, datetime) "
                       "VALUES (%s, %s, %s)")
        
    
        order_data = (order['customer_name'], float(order['grand_total']), datetime.now())
        cursor.execute(order_query, order_data)
        
        
        order_id = cursor.lastrowid

        
        order_details_query = ("INSERT INTO `order_details` "
                               "(order_id, product_id, quantity, total_price) "
                               "VALUES (%s, %s, %s, %s)")
        
        
        order_details_data = []
        for order_details_record in order['order_details']:
            product_id = int(order_details_record['product_id'])
            if not check_product_exists(cursor, product_id):
                print(f"Product ID {product_id} does not exist in the products table.")
                continue
            order_details_data.append((
                order_id,
                product_id,
                float(order_details_record['quantity']),
                float(order_details_record['total_price'])
            ))

        
        if order_details_data:
        
            cursor.executemany(order_details_query, order_details_data)
        
    
        connection.commit()
        return order_id
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()
        return None
def get_all_orders(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM `order`"
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt
        })
    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
    # print(insert_order(connection, {
    #     'customer_name': 'check',
    #     'grand_total': '690',
    #     'order_details': [
    #         {
    #             'product_id': 6,  # Ensure this ID exists in the products table
    #             'quantity': 2,
    #             'total_price': 67
    #         },
    #         {
    #             'product_id': 12,  # Ensure this ID exists in the products table
    #             'quantity': 4,
    #             'total_price': 67
    #         }
    #     ]
    # }))
