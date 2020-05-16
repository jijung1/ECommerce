import mysql.connector
from mysql.connector import Error
import pandas as pd
from faker import Faker


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

    # Create tables if they do not already exist, then add constraints between relations using ALTER TABLE
    print('creating tables for database')
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS
        `ecommerce_site_customer`(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `first_name` varchar(50) NOT NULL,
        `last_name` varchar(50) NOT NULL, 
        `company` varchar(50) NOT NULL, 
        `email` varchar(50) NOT NULL, 
        `ship_street` varchar(50) NOT NULL, 
        `ship_city` varchar(50) NOT NULL, 
        `ship_state` varchar(50) NOT NULL, 
        `ship_country` varchar(50) NOT NULL);
        CREATE TABLE IF NOT EXISTS
        `ecommerce_site_employee`(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
        `first_name` varchar(50) NOT NULL, 
        `last_name` varchar(50) NOT NULL, 
        `title` varchar(50) NOT NULL, 
        `email` varchar(50) NOT NULL);
        CREATE TABLE IF NOT EXISTS
        `ecommerce_site_shipper`(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
        `shipper_name` varchar(64) NOT NULL, 
        `phone` varchar(31) NOT NULL);
        CREATE TABLE IF NOT EXISTS
        `ecommerce_site_supplier`(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
        `supplier_name` varchar(50) NOT NULL, 
        `product_name` varchar(50) NOT NULL, 
        `price` numeric(20, 2) NOT NULL);
        CREATE TABLE IF NOT EXISTS
        `ecommerce_site_product`(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
        `prod_name` varchar(100) NOT NULL, 
        `price` numeric(20, 2) NOT NULL, 
        `units_in_stock` integer NOT NULL, 
        `units_on_order` integer NOT NULL, 
        `supplier_id_id` integer NULL);
        CREATE TABLE IF NOT EXISTS
        `ecommerce_site_order`(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
        `tracking_number` varchar(50) NOT NULL, 
        `status` varchar(50) NOT NULL, 
        `customer_rating` numeric(2, 1) NOT NULL, 
        `bill_street` varchar(50) NOT NULL, 
        `bill_city` varchar(50) NOT NULL, 
        `bill_state` varchar(50) NOT NULL, 
        `bill_country` varchar(50) NOT NULL, 
        `bill_postal_code` varchar(50) NOT NULL, 
        `invoice_total` numeric(20, 2) NOT NULL, 
        `date_ordered` datetime(6) NOT NULL, 
        `date_shipped` datetime(6) NOT NULL, 
        `date_completed` datetime(6) NOT NULL, 
        `customer_id_id` integer NOT NULL, 
        `ship_via_id` integer NOT NULL);
        CREATE TABLE IF NOT EXISTS
        `ecommerce_site_order_product_id`(`id` integer AUTO_INCREMENT NOT NULL PRIMARY  KEY, 
        `order_id` integer NOT  NULL, 
        `product_id` integer NOT NULL);
        ALTER TABLE `ecommerce_site_customer`
        ADD COLUMN `assigned_employee_id` integer NULL, 
        ADD CONSTRAINT `ecommerce_site_custo_assigned_employee_id_5ddfe05b_fk_ecommerce` FOREIGN KEY(`assigned_employee_id`)
        REFERENCES `ecommerce_site_employee`(`id`);
        ALTER TABLE `ecommerce_site_product`
        ADD CONSTRAINT `ecommerce_site_produ_supplier_id_id_8b897f6c_fk_ecommerce`
        FOREIGN KEY(`supplier_id_id`)
        REFERENCES `ecommerce_site_supplier`(`id`);
        ALTER TABLE `ecommerce_site_order`
        ADD CONSTRAINT `ecommerce_site_order_customer_id_id_5500849e_fk_ecommerce`
        FOREIGN KEY(`customer_id_id`)
        REFERENCES `ecommerce_site_customer`(`id`);
        ALTER TABLE `ecommerce_site_order`
        ADD CONSTRAINT `ecommerce_site_order_ship_via_id_24fec581_fk_ecommerce`
        FOREIGN KEY(`ship_via_id`)
        REFERENCES `ecommerce_site_shipper`(`id`);
        ALTER TABLE `ecommerce_site_order_product_id`
        ADD CONSTRAINT `ecommerce_site_order_pro_order_id_product_id_49fecc15_uniq`
        UNIQUE(`order_id`, `product_id`);
        ALTER TABLE `ecommerce_site_order_product_id`
        ADD CONSTRAINT `ecommerce_site_order_order_id_e2aa3877_fk_ecommerce`
        FOREIGN KEY(`order_id`)
        REFERENCES `ecommerce_site_order`(`id`);
        ALTER TABLE `ecommerce_site_order_product_id`
        ADD CONSTRAINT `ecommerce_site_order_product_id_4a132e26_fk_ecommerce`
        FOREIGN KEY(`product_id`) REFERENCES
        `ecommerce_site_product`(`id`); 
    """, multi=True)

    # Reset all tables and import new data
    cursor.execute("DELETE FROM ecommerce_site_order_product_id")
    cursor.execute("DELETE FROM ecommerce_site_order")
    cursor.execute("DELETE FROM ecommerce_site_product")
    cursor.execute("DELETE FROM ecommerce_site_supplier")
    cursor.execute("DELETE FROM ecommerce_site_customer")
    cursor.execute("DELETE FROM ecommerce_site_employee")
    cursor.execute("DELETE FROM ecommerce_site_shipper")
    conn.commit()
    print('importing csv files')
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
    print('inserting suppliers')
    for index, row in df_supplier.iterrows():
        cursor.execute('INSERT INTO ecommerce_site_supplier(id, supplier_name, product_name, price) VALUES (%s,%s,%s,%s)',
                       (row[0], row[1], row[2], row[3],))
        conn.commit()

    print('inserting products')
    #for product, randomly assign  pk of supplier to row[5]
    fake = Faker()
    for index, row in df_product.iterrows():
        cursor.execute(
            'INSERT INTO ecommerce_site_product(id, prod_name, price, units_in_stock, units_on_order, supplier_id_id) VALUES (%s,%s,%s,%s,%s,%s)',
            (row[0], row[1], row[2], row[3],row[4],fake.random_int(min=1, max=len(df_supplier)),))
        conn.commit()
    print('inserting employees')
    for index, row in df_employee.iterrows():
        cursor.execute('INSERT INTO ecommerce_site_employee(id, first_name, last_name, title, email) VALUES (%s,%s,%s,%s,%s)',
                       (row[0], row[1], row[2], row[3], row[4],))
        conn.commit()
    print('inserting customers')
    for index, row in df_customer.iterrows():
        cursor.execute('INSERT INTO ecommerce_site_customer(id, first_name, last_name, company, email, ship_street, ship_city, ship_state, ship_country, assigned_employee_id)'
                       ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], fake.random_int(min=1, max=len(df_employee)),))
        conn.commit()
    print('inserting shippers')
    for index, row in df_shipper.iterrows():
        cursor.execute('INSERT INTO ecommerce_site_shipper(id, shipper_name, phone)'
                       ' VALUES (%s,%s,%s)',
                       (row[0], row[1], row[2],))
        conn.commit()
    print('inserting orders')
    for index, row in df_order.iterrows():
        cursor.execute('INSERT INTO ecommerce_site_order(id, tracking_number, status,'
                       'customer_rating, bill_street, bill_city, bill_state, bill_country,'
                       'bill_postal_code, invoice_total, date_ordered, date_shipped, date_completed,'
                       ' customer_id_id, ship_via_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                        row[11], row[12], fake.random_int(min=1, max=len(df_customer)), fake.random_int(min=1, max=len(df_shipper)),))
        conn.commit()
    print('updating order/product details')
    for i in range(1, 100):
        cursor.execute('INSERT INTO ecommerce_site_order_product_id(id, order_id, product_id) '
                       'VALUES (%s,%s,%s)',
                       (i, fake.random_int(min=1, max=len(df_order)),
                        fake.random_int(min=1, max=len(df_product)),))
        conn.commit() or conn.rollback()
    print('Creating indexes')
    # Create indexes
    cursor.execute('CREATE INDEX product_index on ecommerce_site_product(price)')
    cursor.execute('CREATE INDEX order_index on ecommerce_site_order(date_completed)')
    cursor.execute('CREATE INDEX supplier_index on ecommerce_site_supplier(product_name)')
    cursor.execute('CREATE INDEX employee_index on ecommerce_site_employee(first_name)')
    cursor.execute('CREATE INDEX shipper_index on ecommerce_site_employee(shipper_name)')
    cursor.execute('CREATE INDEX customer_index on ecommerce_site_customer(first_name)')
    conn.commit() or conn.rollback()
