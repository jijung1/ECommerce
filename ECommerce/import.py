import mysql.connector
from mysql.connector import Error
import pandas as pd
from faker import Faker


# read from supplier.csv and return in dataframe
def import_csv(filename):
    return pd.read_csv(filename, header=None)


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='34.83.244.203',
                                       database='ecommerce',
                                       user='user1',
                                       password='spring2020cpsc408')
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)


if __name__ == '__main__':
    conn = connect()
    cursor = conn.cursor()

    # Reset all tables and import new data
    cursor.execute("DELETE FROM ecommerce_site_order_product_id")
    cursor.execute("DELETE FROM ecommerce_site_order")
    cursor.execute("DELETE FROM ecommerce_site_product")
    cursor.execute("DELETE FROM ecommerce_site_supplier")
    cursor.execute("DELETE FROM ecommerce_site_customer")
    cursor.execute("DELETE FROM ecommerce_site_employee")
    cursor.execute("DELETE FROM ecommerce_site_shipper")
    conn.commit() #or conn.rollback()

    df_supplier = import_csv('supplier.csv')
    df_product = import_csv('product.csv')
    df_employee = import_csv('employee.csv')
    df_customer = import_csv('customer.csv')
    df_shipper = import_csv('shipper.csv')
    df_order = import_csv('order.csv')

    """
    handle constraints and prepare data for insertion into database (product has fk to supplier, customer has fk to employee,
    order has fk to customer, order has fk to shipper, and lastly ecommerce_site_order_product_id has fk to order and product.)
    """

    for index, row in df_supplier.iterrows():
        cursor.execute('INSERT INTO ecommerce_site_supplier(id, supplier_name, product_name, price) VALUES (%s,%s,%s,%s)',
                       (row[0], row[1], row[2], row[3],))
        conn.commit()
    #for product, randomly assign  pk of supplier to row[5]
    fake = Faker()
    for index, row in df_product.iterrows():
        cursor.execute(
            'INSERT INTO ecommerce_site_product(id, prod_name, price, units_in_stock, units_on_order, supplier_id_id) VALUES (%s,%s,%s,%s,%s,%s)',
            (row[0], row[1], row[2], row[3],row[4],fake.random_int(min=1, max=len(df_supplier)),))
        conn.commit()
    for index, row in df_employee.iterrows():
        cursor.execute('INSERT INTO ecommerce_site_employee(id, first_name, last_name, title, email) VALUES (%s,%s,%s,%s,%s)',
                       (row[0], row[1], row[2], row[3], row[4],))
        conn.commit()
    for index, row in df_customer.iterrows():
        cursor.execute('INSERT INTO ecommerce_site_customer(id, first_name, last_name, company, email, ship_street, ship_city, ship_state, ship_country, assigned_employee_id)'
                       ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], fake.random_int(min=1, max=len(df_employee)),))
        conn.commit()
    for index, row in df_shipper.iterrows():
        cursor.execute('INSERT INTO ecommerce_site_shipper(id, shipper_name, phone)'
                       ' VALUES (%s,%s,%s)',
                       (row[0], row[1], row[2],))
        conn.commit()
    for index, row in df_order.iterrows():
        cursor.execute('INSERT INTO ecommerce_site_order(id, tracking_number, status, '
                       'customer_rating, bill_street, bill_city, bill_state, bill_country,'
                       'bill_postal_code, invoice_total, date_ordered, date_shipped, date_completed,'
                       ' customer_id_id, ship_via_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                        row[11], row[12], fake.random_int(min=1, max=len(df_customer)), fake.random_int(min=1, max=len(df_shipper)),))
        conn.commit()


"""
1,TNC946108553,Pending_Payment,2,91205 Sawyer Mews Apt. 487,North Matthew,Pennsylvania,Bangladesh,89018,
1621.66,2020-02-18 09:39:15,2020-03-13 16:00:50,2020-04-08 19:20:59


"""


    #df = pd.read_csv('filename')


"""    cursor.execute("SELECT * FROM ecommerce_site_product")
    row = cursor.fetchall()
    print(row)"""
