# pip install mysql-connector
# This package allows Python to connect to a MySQL database.

import mysql.connector # Importing the connector module
# Establishing a connection to the MySQL server
mydb = mysql.connector.connect(
    host = "localhost", # Server location (localhost means your own computer)
    user = "root" , # MySQL username
    password = "Vaishnavi") # MySQL password (make sure this matches your MySQL root password)


# Creating a cursor object to execute SQL commands
cur = mydb.cursor()

str = "create database Bakeryshop_management_system"

# Executing the query
cur.execute(str)
# Closing the connection
mydb.close()