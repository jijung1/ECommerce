from faker import Faker
import csv
import sys
import random


def generate_supplier(num_records):
    fake = Faker()
    csv_file = open('supplier.csv', 'w')
    writer = csv.writer(csv_file)
    for i in range(1, int(num_records)+1):
        writer.writerow([i, fake.bs(), fake.numerify(text='Product %-%%##'),
                         fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=1, max_value=999)])


# Handle constraints using import.py after generating all relation data

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


def generate_shipper(num_records):
    fake = Faker()
    csv_file = open('shipper.csv', 'w')
    writer = csv.writer(csv_file)
    for i in range(1, int(num_records)+1):
        writer.writerow([i, fake.bs(), fake.phone_number()])


def generate_order(num_records):
    fake = Faker()
    csv_file = open('order.csv', 'w')
    writer = csv.writer(csv_file)
    status = ['Initiated', 'Pending_Payment', 'In-Transit', 'Completed', 'Overdue']
    for i in range(1, int(num_records)+1):
        writer.writerow([i, fake.bothify(text="???#########", letters='ACFTCNZXY'),
                         random.choice(status), fake.random_int(min=1, max=5), fake.street_address(), fake.city(),
                        fake.state(), fake.country(), fake.postcode(), fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=999, max_value=9999),
                        fake.date_time_between(start_date='-70d', end_date='-50d'), fake.date_time_between(start_date='-50d', end_date='-30d'), fake.date_time_between(start_date='-30d', end_date='-10d')])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Unexpected Input. Expected Syntax: generate.py <file_name> <num_of_records>")
    else:
        if "supplier.csv" in sys.argv[1].lower():
            generate_supplier(sys.argv[2])
        elif "product.csv" in sys.argv[1].lower():
            generate_product(sys.argv[2])
        elif "employee.csv" in sys.argv[1].lower():
            generate_employee(sys.argv[2])
        elif "customer.csv" in sys.argv[1].lower():
            generate_customer(sys.argv[2])
        elif "shipper.csv" in sys.argv[1].lower():
            generate_shipper(sys.argv[2])
        elif "order.csv" in sys.argv[1].lower():
            generate_order(sys.argv[2])
        else:
            print('Unexpected Input. Expected Syntax: generate.py <file_name> <num_of_records>')
            sys.exit(0)



