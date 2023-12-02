#!/usr/bin/python3
def islower(c):
    asci_of_c = ord(c)
    for i in range(97, 123):
        if i == asci_of_c:
            return True
            break
    else:
        return False
