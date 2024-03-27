import os
import sys

# Get the directory of the current script
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the current script
parent_dir = os.path.dirname(current_script_path)

# Add the parent directory to sys.path
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import database.db_functions.delete as delete
import database.db_functions.update as update
import database.db_functions.select as select
import menu.main as main


class User():

    def __init__(self,first_name='',last_name='',username = '',password='', user_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = username
        self.password = password
        self.user_id = user_id
    

    #edit payment info method
    def edit_payment_info(self, id):
        #Aunthenticate by requesting for password
        while (1):
            print("Enter password")
            user_psd = input()
            if user_psd != self.password:
                print("Incorrect password\t Try again")
                continue
            break       
        ### take payment info from user
        print("\nEnter Payment Details below\n")
        print("Enter payment type:", end='  ')
        payment_type = input()
        #Card number Check
        while (1):
            print("Enter card number:", end='  ')
            try:
                card_number = int(input())
                break
            except:
                print("Incorrect type: Enter Card Number digits\n")
                pass
        #CVV Check
        while (1):
            print("Enter CVV:", end='  ')
            try:
                cvv = int(input())
                break
            except:
                print("Incorrect type: Enter CVV digits\n")
                pass
        print("Enter address line 1:", end='  ')
        address_line_1 = input()
        print("Enter address line 2:", end='  ')
        address_line_2 = input()
        print("Enter city:", end='  ')
        city = input()
        print("Enter state:", end='  ')
        state = input()
        #zip code check
        while (1):
            print("Enter Zip Code:", end='  ')
            try:
                zipcode = int(input())
                break
            except:
                print("Incorrect type: Enter Zip Code digits\n")
                pass
        #phone number check
        while (1):
            print("Enter phone number:", end='  ')
            try:
                phonenumber = int(input())
                break
            except:
                print("Incorrect type: Enter phone number digits\n")
                pass    

        #update payment info in thesystem
        payment_query = "UPDATE Payment_Info SET Payment_Type='%s',Card_Number='%s',CVV = '%s',Address_Line_1='%s',\
        Address_Line_2='%s',City='%s',State='%s',Zip_Code='%s',Phone_Number='%s' WHERE User_ID =%s"\
            %(payment_type, card_number,cvv,address_line_1,address_line_2,city,state,zipcode,phonenumber,id)
        update.update_data(payment_query)
    
    
    #Edit shipping info method
    def edit_shipping_info(self, id):
        #Aunthenticate by requesting for password
        while (1):
            print("Enter password to proceed")
            user_psd = input()
            if user_psd != self.password:
                print("Incorrect password\t Try again")
                continue
            break 
        ### take shipping info from user
        print("\nEnter shipping information below\n")
        print("Enter Address Line 1:", end='  ')
        address_1 = input()
        print("Enter address line 2:", end='  ')
        address_2 = input()
        print("Enter city:", end='  ')
        shipping_city = input()
        print("Enter state:", end='  ')
        shipping_state = input()
        #Zip code check
        while (1):
            print("Enter Zip Code:", end='  ')
            try:
                shipping_zipcode = int(input())
                break
            except:
                print("Incorrect type: Enter Zip Code digits\n")
                pass        
        #phone number check
        while (1):
            print("Enter phone number:", end='  ')
            try:
                shipping_phone = int(input())
                break
            except:
                print("Incorrect type: Enter phone number digits\n")

        #Update shipping info in system
        shipping_query = "UPDATE Shipping_Info SET Address_Line_1='%s',Address_Line_2='%s',City='%s',State='%s', \
            Zip_Code='%s',Phone_Number='%s' WHERE User_ID =%s"\
            %(address_1, address_2,shipping_city,shipping_state,shipping_zipcode,shipping_phone,id)
        update.update_data(shipping_query)


    #Edit username method
    def edit_username(self, id):
        #Aunthenticate by requesting for password
        while (1):
            print("Enter password to proceed")
            user_psd = input()
            if user_psd != self.password:
                print("Incorrect password\t Try again")
                continue
            break
        #requet new username
        while(1):
            print("Enter new username")
            new_username = input()
            if new_username == self.user_name:
                print("Cannot use old username")
                continue
            break
        #update username in the system
        self.user_name = new_username
        username_query = "UPDATE Users SET Username='%s' WHERE User_ID=%s" %(new_username,id)
        update.update_data(username_query)
        


    #Edit Password Method
    def edit_password(self, id):
        #Aunthenticate by requesting for password
        while (1):
            print("Enter old password to proceed")
            user_psd = input()
            if user_psd != self.password:
                print("Incorrect password\t Try again")
                continue
            break 
        #take new password from user
        while(1):
            print("Enter new password")
            new_password = input()
            if new_password == self.password:
                print("Cannot use old password")
                continue
            break
        #update password in the system
        self.password = new_password
        password_query = "UPDATE Users SET Password='%s' WHERE User_ID=%s" %(new_password,id)
        update.update_data(password_query)
    

    #Delete User Account Method
    def delete_user_account(self):
        while (1):
            print("Are you sure? (Y/n)")
            choice = input()
            if choice == 'Y':
                print("Enter password to proceed")
                user_psd = input()
                actual_psd = select.selector("SELECT Password FROM Users where User_ID=%s" %self.user_id)

                if user_psd == actual_psd[0][0]:

                    #delete queries
                    delete_user_query = "DELETE FROM Users WHERE User_ID=%s" %self.user_id
                    delete_payment_query = "DELETE FROM Payment_Info WHERE User_ID=%s" %self.user_id
                    delete_shipping_query = "DELETE FROM Shipping_Info WHERE User_ID=%s" %self.user_id
                    delete_histroy_query = "DELETE FROM User_History WHERE User_ID=%s" %self.user_id
                    delete_cart_history = "DELETE FROM Cart WHERE USER_ID=%s" %self.user_id

                    #delete command execute
                    delete.delete_data(delete_user_query)
                    delete.delete_data(delete_payment_query)
                    delete.delete_data(delete_shipping_query)
                    delete.delete_data(delete_histroy_query)
                    delete.delete_data(delete_cart_history)

                    return True

                else:
                    print("Incorrect password\t Try again")
                    continue
            elif choice == 'n': 
                return False
            else:
                print("Incorrect option: Try again")
