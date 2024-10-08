# !/usr/bin/env python 3
if __name__ == '__main__':

    Password = input("Please create a password: ")

    if 8 <= len(Password) <= 12:
        Confirm = input("Retype your password to confirm it: ")
        if Password == Confirm:
            print("Password created successfully")
        else:
            print("Error: passwords do not match")
    else:
        print("Error: password needs to be 8-12 characters long")
