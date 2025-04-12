import mysql.connector  # Module to connect Python with MySQL


# Connecting to the existing database 'bakeryshop_management_system'
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Vaishnavi", database ="bakeryshop_management_system")

try:
    # Creating the Products table
    cur = mydb.cursor()

    str = '''
    create table Products
    (Id int Primary key, Name varchar(20), Price float, quantity int)
    '''
    cur.execute(str)
    cur.close()

    # Creating the Orders table
    cur = mydb.cursor()
    str = '''
    CREATE TABLE orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        product_id INT,
        product_name VARCHAR(20),
        quantity INT,
        price FLOAT,
        total FLOAT,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        '''
    cur.execute(str)
    cur.close()

     # Creating the Feedback table
    cur = mydb.cursor()
    str = '''
    CREATE TABLE Feedback (
        feedback_id INT AUTO_INCREMENT PRIMARY KEY,
        feedback Varchar(250))
        '''
    cur.execute(str)

except mysql.connector.errors.ProgrammingError:
    print("Table already exits")

else:
    mydb.close()

