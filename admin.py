from bakery import Bakery
from prettytable import PrettyTable
import mysql.connector


# Establish connection to the MySQL database
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Vaishnavi", database ="bakeryshop_management_system")

class Admin:
    
    # Method to add a new product to the database
    def addProduct(self):
        cur = mydb.cursor()
        str = " insert into products values (%s, %s, %s, %s) "
        try:
            # Taking input from the user
            id = int(input("Enter the product ID : "))
            name = input("Enter the Product Name : ")
            price = float(input("Enter the Price : "))
            quantity = int(input("Enter the product Quantity : "))     

        except ValueError:
            # Handle invalid numeric input
            print("Please Enter Numerical Value")

        except :
            # Handle any other exceptions
            print("Something is wrong...")

        else:
            # If all inputs are valid, insert the product into the database

            values = (id,name,price,quantity)
            cur.execute(str,values)
            mydb.commit()
            cur.close()
            print("Product added successfully")


    # Method to display all products in the database

    def displayProduct(self):
        cur = mydb.cursor()
        str = "select * from products"
        cur.execute(str)
        records = cur.fetchall()
        # Using PrettyTable to display in table format
        table = PrettyTable()
        table.field_names = ["Id","Name","Price","Quantity"]
        for r in records:
            table.add_row([r[0],r[1],r[2],r[3]])
        print(table)
        cur.close()

    # Method to search for a specific product by name
    def searchProduct(self,name):
        cur = mydb.cursor(buffered=True)
        str = '''
        select * from products where name = %s
        '''
        values = (name,)
        cur.execute(str,values)
        record = cur.fetchone()
        
        if record:
            # Display product if found
            table = PrettyTable()
            table.field_names = ["ID", "Name", "Price", "Quantity"]
            table.add_row([record[0], record[1], record[2], record[3]])
            print(table)
        else:
             # Inform if not found
            print(f"Sorry, we couldn't find a product named {name} in our bakery menu")
        cur.close()

    # Method to update product details by ID
    def updateProduct(self, id):
        cur = mydb.cursor(buffered=True)
        str = '''
        select * from Products where id = %s
        '''
        values = (id,)
        cur.execute(str,values)
        record = cur.fetchone()
        
        if record:
            # Show existing product details
            table = PrettyTable()
            table.field_names = ["ID", "Name",  "Price", "Quantity"]
            table.add_row([record[0], record[1], record[2], record[3]])
            print(table)
            # Ask and update name
            ans = input("Do you wnat to change the name (y/n) ? : ")
            if ans=="y" or ans=="Y":
                cur = mydb.cursor()
                str = '''
                update products
                set name = %s where id = %s 
                '''
                name = input("Enter the New name : ")
                values = (name,id)
                cur.execute(str,values)
                mydb.commit()
                print()
                print("Updated successufully")

            # Ask and update price
            ans = input("Do you wnat to change the Price (y/n) ? : ")
            if ans=="y" or ans=="Y":
                cur = mydb.cursor()
                str = '''
                update products
                set price = %s where id = %s 
                '''
                price = int(input("Enter the new Price : "))
                values = (price,id)
                cur.execute(str,values)
                mydb.commit()
                print()
                print("Updated successufully")

            # Ask and update quantity
            ans = input("Do you wnat to change the Quantity (y/n) ? : ")
            if ans=="y" or ans=="Y":
                cur = mydb.cursor()
                str = '''
                update products
                set quantity = %s where id = %s 
                '''
                quantity = int(input("Enter the new Price : "))
                values = (quantity,id)
                cur.execute(str,values)
                mydb.commit()
                print()
                print("Updated successufully")

        elif not record:
             # Inform if product ID is not found
            print(f"Sorry, we couldn't find a product Id {id} in our bakery menu")
            return

    # Method to delete a product by ID   
    def deleteProduct(self, id):
        cur = mydb.cursor(buffered=True)
        str = '''
        select * from products where id = %s
        '''
        values = (id,)
        cur.execute(str,values)
        record = cur.fetchone()
        
        if record:
            # If product exists, delete it
            cur = mydb.cursor()
            str = '''
            delete from products
            where id = %s
            '''
            values = (id,)
            cur.execute(str,values)
            mydb.commit()
            cur.close()
            print("Product deleted succesfully ..")
        
        elif not record:
                # Inform if not found
                print(f"Sorry, we couldn't find a product Id {id} in our bakery menu")
                return

    # Method to display all feedback entries
    def displayFeedback(self):
        cur = mydb.cursor()
        str = "select * from feedback"
        cur.execute(str)
        records = cur.fetchall()
        # Display feedback in tabular format
        table = PrettyTable()
        table.field_names = ["Id","Feedback"]
        for r in records:
            table.add_row([r[0],r[1]])
        print(table)
        cur.close()
        mydb.close()
    

        