from bakery import Bakery
from prettytable import PrettyTable
import mysql.connector

# Establishing connection with MySQL database
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Vaishnavi", database ="bakeryshop_management_system")
class User:


    # Method to display all available products in the bakery
    def displayProduct(self):
        cur = mydb.cursor()
        str = "select * from products"
        cur.execute(str)
        records = cur.fetchall()
        # Display results using PrettyTable
        table = PrettyTable()
        table.field_names = ["Id","Name","Price","Quantity"]
        for r in records:
            table.add_row([r[0],r[1],r[2],r[3]])
        print(table)
        cur.close()

     # Method to search for a product by name
    def searchProduct(self,name):
        cur = mydb.cursor(buffered=True)
        str = '''
        select * from products where name = %s
        '''
        values = (name,)
        cur.execute(str,values)
        record = cur.fetchone()
        
        if record:
            # Show product details if found
            table = PrettyTable()
            table.field_names = ["ID", "Name", "Price", "Quantity"]
            table.add_row([record[0], record[1], record[2], record[3]])
            print(table)
        else:
             # Inform if product is not found
            print("Product not found")
        cur.close()

   # Method to place an order
    def placeOrder(self,product_name,buy_quantity):
        # Step 1: Check if product exists and fetch its details
        cur = mydb.cursor(buffered=True)
        str = '''
        select * from products where name = %s
        '''
        values = (product_name,)
        cur.execute(str,values)
        record = cur.fetchone()
        cur.close()

        if record:
            # Extract product details       
            available_quantity = record[3]
            price = record[2]
            product_name = record[1]
            product_id = record[0]

            # Step 2: Check stock availability
            if buy_quantity > available_quantity:
                print("oops available quantity is only ",available_quantity)

            else:
                # Step 3: Place the order and insert into 'orders' table
                total = price * buy_quantity
                cur = mydb.cursor(buffered=True)
                str = '''
                INSERT INTO orders (product_id, product_name, quantity, price, total)
                VALUES (%s, %s, %s, %s, %s)
                '''
                value = (product_id, product_name, buy_quantity, price, total)
                cur.execute(str, value)
                mydb.commit()
                cur.close()
                # Step 4: Get the last inserted order ID
                cur = mydb.cursor()
                str = "SELECT LAST_INSERT_ID()"
                cur.execute(str)
                last_order_id = cur.fetchone()[0]
                mydb.commit()
                cur.close()
                # Step 5: Update the product quantity
                cur = mydb.cursor(buffered=True)
                str = '''
                UPDATE products
                SET quantity = quantity - %s
                WHERE name = %s
                '''
                values = (buy_quantity, product_name)
                cur.execute(str,values)
                mydb.commit()
                cur.close()
                # Step 6: Fetch and display the recent order details
                cur = mydb.cursor()
                str = "SELECT * FROM orders WHERE order_id = %s"
                cur.execute(str, (last_order_id,))
                records = cur.fetchone()
                cur.close()
                if records:
                    table = PrettyTable()
                    table.field_names = ["order Id","product id","Name","Quantity","Price","total","order date"]                    
                    table.add_row([records[0],records[1],records[2],records[3],records[4],records[5],records[6]])
                    print("Recent Order : ")
                    print(table)
                else:
                    print("Could not fetch the order details")
                
        else:
            # Inform if the product is not found
            print("product not found")

    # Method to add user feedback
    def addFeedback(self):
        cur = mydb.cursor()
        str = " insert into feedback(feedback ) values (%s) "
        feedback = input("Enter the feedback  : ")
        values = (feedback,)
        cur.execute(str,values)
        mydb.commit()
        cur.close()
        print("Thank you for feedback")
        mydb.close()

                