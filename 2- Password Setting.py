# !/usr/bin/env python 3
if __name__ == '__main__':

    Password = input("Please create a password: ")
    Confirm = input("Retype your password to confirm it: ")
    if Password == Confirm:
        print("Password created successfully")
    else:
        print("Error: passwords do not match")
