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
import database.db_functions.insert as insert
import classes.users as users
import login.user_login as user_login
import random

#USER VARIABLES
first_name='' 
last_name='' 
username='' 
password=''
userid=0

#Payment_Info Variables
paymentid=0 
payment_type='' 
card_number=0
cvv=0
address_line_1=''
address_line_2=''
city=''
state=''
zipcode=0
phonenumber=0

#SHIPPING VARIABLES
shippingid=0
userid=0
address_1='' 
address_2=''
shipping_city=''
shipping_state=''
shipping_zipcode=0
shipping_phone=0


#create account method
def create_account():

    random.seed()
    userid = -1
    paymentid = -1
    shippingid = -1
    
    #generate random integer for user id
    while(1):
        userid = random.randint(0,10000) #generate random number for user id
        temp1 = "SELECT user_id FROM Users WHERE User_ID = %s" %userid
        id = select.selector(temp1)
        if not id: break   
    #generate payment id
    while(1):
        paymentid = random.randint(0,10000) #generate random number for user id
        temp2 = "SELECT Payment_ID FROM Payment_Info WHERE Payment_ID = %s" %paymentid
        pay_id = select.selector(temp2)
        if not pay_id: break
    #generate shipping id
    while(1):
        shippingid = random.randint(0,10000) #generate random number for user id
        temp3 = "SELECT Shipping_ID FROM Shipping_Info WHERE Shipping_ID = %s" %shippingid
        ship_id = select.selector(temp3)
        if not ship_id: break



    ### Take user info
    print("\nEnter Personal Details below\n")
    print("Enter first Name")
    first_name = input()
    print("Enter last name")
    last_name = input()
    username = ''
    while (1):
        print("Enter username")
        username = input()
        # check username from User table
        usr_cmd= "SELECT username FROM Users WHERE Username = '%s'" %username
        user_details = select.selector(usr_cmd)
        if not user_details: break
        print("Username already exists\nUse a different username")
    print("Enter password")
    password = input()
    
    

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
            print("Incorrect type: Enter Zip Code digits\n")
            pass
    
    ## insert into Users table
    user_query = "INSERT INTO Users (First_Name, Last_Name, Username, Password, User_ID) VALUES ('%s','%s','%s','%s','%s')"\
                %(first_name, last_name, username, password,userid,)
    insert.insert_data(user_query)
    
    ## insert into Payment table
    payment_query = "INSERT INTO Payment_Info (Payment_ID, User_ID, Payment_Type, Card_Number, CVV,\
        Address_Line_1, Address_Line_2, City, State, Zip_Code, Phone_Number) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
        %(paymentid, userid, payment_type, card_number,cvv,address_line_1,address_line_2,city,state,zipcode,phonenumber,)
    insert.insert_data(payment_query)        

    ## insert into Shipping Info table
    shipping_query = "INSERT INTO Shipping_Info (Shipping_ID, User_ID, Address_Line_1, Address_Line_2,\
        City, State, Zip_Code, Phone_Number) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"\
        %(shippingid, userid, address_1, address_2,shipping_city,shipping_state,shipping_zipcode,shipping_phone,)
    insert.insert_data(shipping_query)

    print("\nSuccessfully created account")

    ### Proceed to login page
    print("Proceeding to login page\n")

    current_user = users.User(first_name,last_name,username,password,userid)
    user_login.login_page(current_user, userid)
