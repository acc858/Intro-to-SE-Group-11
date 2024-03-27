import os
import sys

# Get the directory of the current script
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the current script
parent_dir = os.path.dirname(current_script_path)

# Add the parent directory to sys.path
if parent_dir not in sys.path:
    sys.path.append(parent_dir)




import create_account.create as create
import login.user_login as user_login

def main_func():
    while (1):
        print("\n1. Login\n2. Create Account\n3. Exit Program")
        choice = -1
        try:
            choice = int(input())
        except:
            print("\nIncorrect option\Try again")
            continue
        if choice == 1: 
            user_login.login()
        elif choice == 2:
            create.create_account()
        elif choice == 3:
            print("\nExiting...Good bye!\n")
            sys.exit()
        else:
            print("Incorrect option: Try again")
        
    sys.exit()


if __name__ == '__main__':
    
    main_func()
