#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list == [] or my_list is None:
        pass
    elif idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        new_list = my_list[:]
        for i in range(len(my_list)):
            if i == idx:
                new_list[i] = element
        return new_list
