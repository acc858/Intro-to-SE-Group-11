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
import database.db_functions.delete as delete
import database.db_functions.update as update



def view_user_history(user_id):
    history_query = "SELECT * FROM User_History WHERE USER_ID = '%s'" %user_id
    history_result = select.selector(history_query)

    output_format ="ISBN= %s, Title='%s', Author='%s', Year=%s, Genre='%s', Quantity=%s, Price=$%s"
    #print out user history to user
    for data in history_result:
        print(output_format %(data[0],data[1],data[2],data[3],data[4],data[6],data[7]))


def add_to_user_history():
    #select everything grom the cart
    data = select.selector("SELECT * FROM Cart") 

    for x in data:
        #check if item alreaady exits in user history
        ISBN = x[0]
        tmp = select.selector("SELECT Quantity FROM User_History WHERE ISBN=%s" %ISBN)

        # if item already exits in user history, increment the item quantity
        if tmp:
            query = "UPDATE User_History SET Quantity=%s WHERE ISBN=%s" %(x[6]+tmp, ISBN)
            update.update_data(query)
        else:
            #insert it into user history cart
            query = "INSERT INTO User_History (ISBN, Title, Author, Year, Genre, User_ID, Quantity, Price) \
                VALUES (%s,'%s','%s',%s,'%s',%s,%s,%s)" \
                %(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
            insert.insert_data(query)
