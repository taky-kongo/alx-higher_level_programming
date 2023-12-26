#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    for i in my_list:
        if y == x:
            break
        else:
            print(i, end="")
        y += 1
    print()
    return y
