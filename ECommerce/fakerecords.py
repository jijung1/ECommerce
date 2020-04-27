from faker import Faker
import pandas as pd
import csv
import sys
import datetime

#expect as terminal args: python generate.py file_name number_of_records
#so Shipper.csv, Employee.csv, Customer.csv …

"""
def generate_fake_customer_csv():
    fake = Faker()
    # print(fake.name(), fake.address(), fake.city(), fake.phone_number())
    csv_file = open('customer.csv', 'w')
    writer = csv.writer(csv_file)
    for x in range(1, 10):
        writer.writerow([x,fake.first_name(), fake.last_name(), fake.company(),fake.street_address(),fake.city(), fake.state(),fake.country()])

generate_fake_customer_csv()

"""


def generate_supplier(num_records):
    fake = Faker()
    csv_file = open('supplier.csv', 'w')
    writer = csv.writer(csv_file)
    for i in range(1, int(num_records)+1):
        writer.writerow([i, fake.bs(), fake.numerify(text='Product %-%%##'),
                         fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=1, max_value=999)])


#Handle constraints separately after generating all relation data
def generate_product(num_records):
    fake = Faker()
    csv_file = open('product.csv', 'w')
    writer = csv.writer(csv_file)
    for i in range(1, int(num_records)+1):
        writer.writerow([i, fake.numerify(text='Product %-%%##'), fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=999, max_value=9999),
                        fake.pyint(min_value=0, max_value=999), fake.pyint(min_value=0, max_value=100), None])


def generate_employee(num_records):
    fake = Faker()
    csv_file = open('employee.csv', 'w')
    writer = csv.writer(csv_file)
    for i in range(1, int(num_records)+1):
        writer.writerow([i, fake.first_name(), fake.last_name(), fake.job(), fake.email()])

def generate_customer(num_records):
    fake = Faker()
    csv_file = open('customer.csv', 'w')
    writer = csv.writer(csv_file)
    for i in range(1, int(num_records)+1):
        writer.writerow([i, fake.first_name(), fake.last_name(), fake.bs(), fake.email(), fake.street_address(), fake.city(), fake.state(), fake.country(), None])
"""
fake.street_address()
fake.city()
fake.state()
fake.date_time_between(start_date='-70d', end_date='-50d')
fake.pydecimal(right_digits=2, positive=True, min_value=.99, max_value=999.99)

classCustomer(models.Model):
first_name=models.CharField(max_length=50)
last_name=models.CharField(max_length=50)
company=models.CharField(max_length=50)
email=models.EmailField(max_length=50)
ship_street=models.CharField(max_length=50)
ship_city=models.CharField(max_length=50)
ship_state=models.CharField(max_length=50)
ship_country=models.CharField(max_length=50)
assigned_employee=models.ForeignKey(Employee,on_delete=models.SET_NULL)




"""
if __name__ == "__main__":
    if len(sys.argv) != 3:
       print("Unexpected Input. Expected Syntax: generate.py <file_name> <num_of_records>")
    else:
        #continue on sys.argv[1] is name of csv file, sys.argv[2] is number of records to generate
        #file_name should determine which generation sequence to run
        #if file name employee in filename, then run generate_employee(num_records)
        if "supplier" in sys.argv[1].lower():
            generate_supplier(sys.argv[2])
        elif "product" in sys.argv[1].lower():
            generate_product(sys.argv[2])
        elif "employee" in sys.argv[1].lower():
            generate_employee(sys.argv[2])
        elif "customer" in sys.argv[1].lower():
            generate_customer(sys.argv[2])
        else:
            print('u done f''d up')








"""
data = pd.read_csv("customer.csv", header=None)
print(data.head())


"""

