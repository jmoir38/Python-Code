# !/usr/bin/env python 3
if __name__ == '__main__':

    def case_count(string):
        upper = 0
        lower = 0
        for character in string:
            if character.isupper():
                upper += 1
            elif character.islower():
                lower += 1
        print(f"Uppercase Letters: {upper}")
        print(f"Lowercase Letters: {lower}")

    a = str(input("Enter a string: "))
    case_count(a)
