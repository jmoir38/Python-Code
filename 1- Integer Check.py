# !/usr/bin/env python 3
if __name__ == '__main__':

    def integer_check(num):
        if 0 > num or num > 100:
            print(False)
        else:
            print(True)

    n = int(input("Enter a number between 1 and 100: "))
    integer_check(n)
