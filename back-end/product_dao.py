import mysql.connector
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
             "FROM gs.products INNER JOIN gs.uom ON uom.uom_id = products.uom_id LIMIT 0, 1000;")
    cursor.execute(query)

    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = "INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)"
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    connection.commit()
    return cursor.rowcount


if __name__ == '__main__':
    connection = get_sql_connection()
    # Uncomment to test other functions
    # insert_new_product(connection, {
    #     'product_name': 'Bhindi',
    #     'uom_id': 2,
    #     'price_per_unit': 50
    # })
    # deleted_rows = delete_product(connection, 10)
    # print(f"Number of deleted rows: {deleted_rows}")
    # print(get_all_products(connection))
