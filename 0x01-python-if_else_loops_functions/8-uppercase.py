#!/usr/bin/python3
def uppercase(str):
    str = str + "\n"
    for i in range(len(str)):
        char = str[i]
        asci_of_char = ord(char)
        if asci_of_char >= 97 and asci_of_char <= 122:
            print("{}".format(chr(asci_of_char - 32)), end="")
        else:
            print("{}".format(char), end="")
