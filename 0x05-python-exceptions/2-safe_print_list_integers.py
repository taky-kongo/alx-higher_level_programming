#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    y = 0
    for i in my_list:
        try:
            if y == x:
                break
            print("{:d}".format(i), end="")
            nb_print += 1
            y += 1
        except NameError as nameErr:
            print(nameErr)
        except Exception:
            y += 1
            pass
    if x > y:
        raise IndexError()
    print()
    return nb_print
