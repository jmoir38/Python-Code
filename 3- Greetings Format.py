# !/usr/bin/env python 3
if __name__ == '__main__':

    name = input("Hi! What is your name?\n")
    name = name.title()

    if name:
        print(f"Hello, {name}. Nice to meet you!")
    else:
        print("Hello, Stranger!")