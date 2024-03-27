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
import database.db_functions.delete as delete
import database.db_functions.update as update

class Inventory:

    def __init__(self):
        self


    #increases the stock count of the item
    def increase_inv_item(self,ISBN, quantity):

        try:
            original_qnt = select.selector("SELECT Quantiy FROM Inventory WHERE ISBN='%s'" %ISBN)
            new_quantity = original_qnt + quantity
            query = "UPDATE inventory SET Quantiy = %s WHERE ISBN = '%s'" %(new_quantity, ISBN)
            return True
        except:
            return False


    # pass in isbn and grab the inventory quanity 
    # decrement stock quantiy
    # if stock quantity becomes 0, remove from inventory
    def decrease_inv_item(self, ISBN):
        grab_item_details_query = "SELECT * FROM Inventory WHERE ISBN=%s" %ISBN
        item_details = select.selector(grab_item_details_query)
        item_quantity = item_details[0][5]

        # when item quantity in inventory becomes zero, remove from inventory
        if (item_quantity - 1) == 0: 
            delete.delete_data("DELETE FROM Inventory WHERE ISBN=%s" %ISBN) 
            return 
        #else update new item quantity in inventory
        update.update_data("UPDATE Inventory SET Quantity=%s WHERE ISBN=%s" %(item_quantity-1, ISBN))



    #display the contents in the inventory
    def display_inventory(self):
        inventory_result = select.selector("SELECT * FROM Inventory")

        count = 1
        output_format ="%s. ISBN= %s, Title='%s', Author='%s', Year=%s, Genre='%s', Quantity=%s, Price=$%s"
        #print out inventory to user
        for data in inventory_result:
            print(output_format %(count,data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
            count += 1
