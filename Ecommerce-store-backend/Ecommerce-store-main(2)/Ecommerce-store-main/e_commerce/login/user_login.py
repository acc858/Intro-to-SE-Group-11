import os
import sys

# Get the directory of the current script
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the current script
parent_dir = os.path.dirname(current_script_path)

# Add the parent directory to sys.path
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import database.db_functions.select as select
import classes.inventory as inventory
import classes.users as user
import login.user_history as user_history
import menu.main as main
import classes.inventory as inventory
import classes.order as order
import classes.cart as cart
import login.user_crypto as crypto
import sys


#LOGIN method
def login():
    while (1):
        print("Enter username or enter 'BACK' to go back")
        user_name = input()

        if user_name == "BACK": break
            
        # check username from User table
        #usr_cmd = "SELECT username,password FROM Users WHERE Username = '%s'" %user_name
        usr_cmd= "SELECT username,password,first_name,last_name, user_id FROM Users WHERE Username = '%s'" %user_name
        user_details = select.selector(usr_cmd)
        if not user_details:
            print("Incorrect Username\tTry again\n")
            continue
        Corrent_password = user_details[0][1] #string edit to get actual username for comparison

        print("Enter password")
        password = input()
        password = crypto.encrypt(password)
        if password != Corrent_password:
            print("Incorrect password\n")
            continue

        #Update user details        
        first_name = user_details[0][0]
        last_name = user_details[0][1]
        username = user_details[0][2]
        user_id = user_details[0][4]

        #create User Object
        current_user = user.User(first_name,last_name,username,password,user_id)


        # PROCEED to login page if password and email successfully matches
        login_page(current_user, user_id)
        break


    ### SUCCESSFUL LOGIN PAGE
def login_page(current_user, userid):
    while(1):    
        print("\n1. Edit user settings\
            \n2. Shop\
            \n3. Cart Information\
            \n4. User History\
            \n5. Logout\
            \n6. Exit Program")
        option = -1
        #testing for correct input type
        try:
            option = int(input())
        except:
            print("Incorrect input type\tEnter option 1-6\n")
            continue
        
        #Edit User Settings block
        if option == 1:
            while (1):
                print("\n1. Edit payment information\
                    \n2. Edit shipping information\
                    \n3. Edit username\
                    \n4. Edit password\
                    \n5. Delete User Account\
                    \n6. Go back\n")
                try:
                    user_input = int(input())

                    #edit user payment info
                    if user_input == 1:
                        current_user.edit_payment_info(userid)
                        print("Successfully edited payment information")
                        continue

                    #edit user shipping info
                    elif user_input == 2:
                        current_user.edit_shipping_info(userid)
                        print("Successfully edited shipping information\n")
                        continue

                    #edit username
                    elif user_input == 3:
                        current_user.edit_username(userid)
                        print("Successfully edited username\n")
                        continue

                    elif user_input == 4:
                        current_user.edit_password(userid)
                        print("Successfully changed password\n")

                    #delete user acount 
                    elif user_input == 5: 
                        res = current_user.delete_user_account()
                        if res:
                            print("Successfully deleted account\n")
                            main.main_func()
                        print()
                        continue

                    # go back to previous page block
                    elif user_input == 6: 
                        print("Going back")
                        break
                    else: #if input is incorrect
                        print("incorrect option\nTry again")
                        continue
                except:
                    print("Incorrect input type\nSelect from option 1-4\n")
                    continue

        #Shop block
        elif option == 2:
            usr_order = order.Order(userid)
            while(1):
                try:
                    print("\n1. View items\n2. Add to cart\n3. GO back")
                    usr_option = int(input())
                except:
                    print("Incorrect type input\tTry again")
                    continue
                    
                #display inventory items to user
                if usr_option == 1:
                    print("Displaying items in the Inventory below\n==============================================")
                    inventory_object = inventory.Inventory()
                    inventory_object.display_inventory()
                    print()
                    continue
                
                #if user wants to add to order
                elif usr_option == 2:
                    usr_order.add_item()

                #if user wants to go bak    
                elif usr_option == 3:
                    print("Going back\n")
                    break
                else:
                    print("Incorrect option. Choose from option 1-3\n")

        elif option == 3:
        #     cart_information()
            usr_cart = cart.Cart(userid)
            while(1):
                #print out menu to user
                print("1. View Cart\n2. Remove item from cart\n3. Checkout items in cart\n4. Go back")
                
                #check input type
                try:
                    choice = int(input())
                except:
                    print("Incorrect type: Choose between option 1-4")
                    continue

                #display content in cart for user
                if choice == 1:
                    print("Displaying items in the Cart below\n==============================================")
                    usr_cart.view_cart()
                    continue

                # remove an item from cart
                elif choice == 2:
                    print("Enter item ISBN to remove from cart")
                    try:
                        item_remove = int(input())
                        print()
                    except:
                        print("Incorrect input: Try again")
                        continue

                    usr_cart.remove_from_cart(item_remove)
                    print("Removed ISBN %s from cart" %item_remove)
                    continue

                # checkout block
                elif choice == 3:
                    print("Checking out...")
                    usr_cart.checkout()
                    print("Successfully checked out\n")
                    break

                elif choice == 4:
                    print("Going back")
                    break

                #incorrect option block
                else:
                    print("Incorrect input option: Try option 1-4")
                    continue

                break

        #User History
        elif option == 4:
            while(1):
                print("\n1. View User history\n2. Go back")
                try:
                    usr_choice = int(input())
                except:
                    print("Incorrect input type:  Enter option '1' or '2'")
                    continue
                if usr_choice == 1: 
                    user_history.view_user_history(userid)
                    continue
                elif usr_choice == 2:
                    break
                else: print("Incorrect option")

        #Goes back to Pre-login Page
        elif option == 5:
            print("logging out\n")
            main.main_func()

        #Exits the program
        elif option == 6:
            print("Exiting\n")
            sys.exit()
        #handles wrong option input from user
        else:
            print("Wrong input:\tTry again\n")
    