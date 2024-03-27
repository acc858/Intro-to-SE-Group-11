import os
import sqlite3
import sys
def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)

def insert_data(query):
    ## attempts to connect to the database
    try:
        connection = sqlite3.connect("sqlite.db")

    except:
        print("Failed connection.")

        ## exits the program if unsuccessful
        sys.exit()

    ## cursor to send queries through
    cursor = connection.cursor()
    cursor.execute(query) # insert into table
    connection.commit() # commit changes

    cursor.close()
    connection.close()
