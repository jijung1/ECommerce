import mysql.connector
from mysql.connector import Error
import pandas as pd

# read from supplier.csv, validate data, and insert into database
def import_supplier():
    df = pd.read_csv('supplier.csv', header=None)
    for index, row in df.iterrows():
        print(index, row[0], row[1])



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
    import_supplier()


    #df = pd.read_csv('filename')


"""    cursor.execute("SELECT * FROM ecommerce_site_product")
    row = cursor.fetchall()
    print(row)"""
