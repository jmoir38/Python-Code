# !/usr/bin/env python 3
if __name__ == '__main__':

    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    Password = input("Please create a password: ")

    if Password not in BAD_PASSWORDS:
        if 8 <= len(Password) <= 12:
            Confirm = input("Retype your password to confirm it: ")
            if Password == Confirm:
                print("Password created successfully")
            else:
                print("Error: passwords do not match")
        else:
            print("Error: password needs to be 8-12 characters long")
    else:
        print("Error: choose a better password")
