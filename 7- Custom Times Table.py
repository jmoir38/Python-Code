# !/usr/bin/env python 3
if __name__ == '__main__':

    number = int(input("Please enter a number between 0 and 12:\n"))
    if 0 <= number <= 12:
        for n in range(13):
            print(f" {n} x {number} = {n * number}")
    else:
        print("That is not a number between 0 and 12.\n")
