# !/usr/bin/env python 3
if __name__ == '__main__':

    number = int(input("Please enter a number between -12 and 12 (negative numbers display times table in reverse):\n"))
    if 0 <= number <= 12:
        for n in range(13):
            print(f" {n} x {number} = {n * number}")
    elif -12 <= number <= 0:
        number = abs(number)
        for n in range(12, -1, -1):
            print(f" {n} x {number} = {n * number}")
    else:
        print("That is not a number between 0 and 12.\n")
