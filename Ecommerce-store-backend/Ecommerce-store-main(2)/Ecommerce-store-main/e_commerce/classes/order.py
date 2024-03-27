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
import database.db_functions.update as update
import classes.inventory as inventory

class Order():

    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def add_item(self):
        while(1):
            # take input from user
            print("Enter a valid item ISBN to add to cart or 'BACK' to go back to Shopping page")
            item_id = input()

            #if user decides to go back , go back
            if item_id == "BACK": 
                print()
                break

            #check incorrect input
            try: item_id = int(item_id)
            except:
                print("Incorrect response:  Try again")
                continue

            #get the stock quantity
            item_result = select.selector("SELECT * from Inventory WHERE ISBN=%s" %item_id)
            # if there is no quantity then item does not exit
            if not item_result:
                print("ISBN number does not exit. Try again")
                continue
            
            #get current quantity from cart
            result = select.selector("SELECT Quantity, Price from Cart WHERE ISBN=%s" %item_id)
            item_qnt = 0

            #update current order by adding 1 quantity in user cart
            if result:
                item_qnt = int(result[0][0]) + 1
                item_price = int(result[0][1]) * item_qnt
                update_query = "UPDATE Cart SET Quantity=%s, Price=%s WHERE ISBN=%s" %(item_qnt,item_price,item_id)
                update.update_data(update_query)
            #else insert into user cart
            else: 
                item_qnt = 1
                add_query = "INSERT INTO Cart (ISBN, Title, Author, Year,Genre, User_ID,\
                    Quantity, price) VALUES (%s,'%s','%s',%s,'%s',%s,%s,%s)"\
                    %(item_result[0][0],item_result[0][1],item_result[0][2],item_result[0][3],item_result[0][4],self.user_id,item_qnt, item_result[0][6],)
                insert.insert_data(add_query)
            #drecrease stock quantity
            current_inventory = inventory.Inventory()
            current_inventory.decrease_inv_item(item_id)
            print("Added item %s to cart" %item_id)
            continue
 