from admin import Admin
from user import User
import random
# Creating instances of Admin and User classes
admin = Admin()
user = User()
# Main menu control variables
choice = 0
ch = 0
while choice != 3 :
    print()
    print("------------------------------  Welcome to Moon pie    ----------------------------------")
    print()
    print("\t\t1.Admin")
    print("\t\t2.User")
    print("\t\t3.Exit")
    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Please Enter numerical Value ...")
        continue  # Go back to menu if input is invalid

     # Admin login section
    if choice == 1 :
        username = input("Enter the User Name : ")
        password = input("Enter the password : ")
        # Generate and verify OTP
        otp = random.randint(1000,9999)
        if username == "moonpie" and password == "admin123" :
            print(otp)
            u_otp = int(input("Enter the otp : "))
            if otp == u_otp :
                # Admin operations menu
                while ch != 7:
                    print()
                    print("-------------------------------   Welcome ! you are logged in Admin ! --------------------------------------- ")
                    print()
                    print("\t\t1.Add new Product ")
                    print("\t\t2.Display All Products ")
                    print("\t\t3.Search Product ")
                    print("\t\t4.Update Product")
                    print("\t\t5.Delete Product")
                    print("\t\t6.Display Feedbacks")
                    print("\t\t7.Exit")
                    ch = int(input("enter the choice : "))

                    if ch == 1 :
                        admin.addProduct()
                    
                    elif ch == 2 :
                        admin.displayProduct()

                    elif ch == 3 :
                        name = input("Enter product name : ")
                        admin.searchProduct(name)
                    
                    elif ch == 4 :
                        id = int(input("Enter the id : "))
                        admin.updateProduct(id)

                    elif ch== 5 :
                        id = int(input("Enter the id : "))
                        admin.deleteProduct(id)

                    elif ch == 6 :
                        admin.displayFeedback()
            
            else:
                print("Invalid Otp... please Try Again...")

        else:
            print("Incorrect User name or Password ... please Try Again... ")   
    # User menu
    elif choice == 2 :
        while ch != 5:
            print()
            print("----------------------------------  Welcome ! you are logged in User ! ---------------------------------------")
            print()  
            print("\t\t1.Display All Products ")
            print("\t\t2.Search Product ")
            print("\t\t3.Place order")
            print("\t\t4.Enter feedback")
            print("\t\t5.Exit")
            ch = int(input("enter the choice : "))

            if ch == 1 :
                user.displayProduct()

            elif ch == 2 :
                name = input("Enter product name : ")
                user.searchProduct(name)

            elif ch == 3 :
                product_name = input("Enter the Product name you want to buy: ")
                buy_quantity = int(input("Enter the Quantity: "))
                user.placeOrder(product_name,buy_quantity)

            elif ch == 4 :
                user.addFeedback()
    elif choice == 3:
        print("Thank you for using Moon Pie Bakery Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose from Admin, User or Exit.")
        

