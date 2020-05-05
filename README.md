
# ECommerce Website Documentation

* CPSC408 Project Members:
  * Jin Jung
  * Alex Jones

**ASSIGNMENT 3**

  * Database Schema Diagram is avaiable to view under ECommerce/CPSC408_Documentation/schema
  * fakerecords.py is the utility used to populate csv files with fake data for this database, and it located in       ECommerce/ECommerce/fakerecords.py.
    * Usage: Run program using the command python fakerecords.py <filename> <number of records>, where filename is restricted to the following: ['customer.csv', 'employee.csv', 'shipper.csv', 'order.csv', 'employee.csv', 'supplier.csv', 'product.csv'].
    * Note that the order_product_id table is generated in import.py since it only has order_id and product_id as its attributes.     
  * import.py is the program that will read in the generated csv files, connect to the mysql server, create required tables if they don't already exist, then insert fake data into the database. import.py is located in ECommerce/ECommerce/import.py.
     * Usage: Run program using the command python import.py. The program is currently set up to connect to our project's GCP database, and the user/password info is left in the file because we trust our Rene.
  


**How to set up the environment**
clone repository <br>
open project in pycharm </br>
pip install django <br>


**References**

* Article links</br>
  * https://acquire.io/blog/problems-solutions-ecommerce-faces/</br>
  * https://retailnext.net/en/blog/the-influence-of-database-in-the-retail-industry/</br>
  * http://archive.ics.uci.edu/ml/machine-learning-databases/00352/</br>

* Data Visualization References</br>
  *https://mdbootstrap.com/docs/jquery/javascript/charts/</br>
  
* Local Memory-Caching for responsive website</br>
  *https://data-flair.training/blogs/django-caching/</br>
  
* Performing Raw SQL Queries that return model instances</br>
  * https://docs.djangoproject.com/en/3.0/topics/db/sql/</br>

**Reasons to Use Django**</br>
* What is it? </br>
  * Django is a python web framework that uses the data flow shown below to </br>

  *![basic-django](https://user-images.githubusercontent.com/47117122/78516764-99955f80-776f-11ea-9eff-3eddbe685732.png)

* Batteries Included
  * https://docs.djangoproject.com/en/3.0/

**Purpose**
  * Provide competitive analysis/visualization tools as well as administrative (CRUD) functionality.
