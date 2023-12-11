#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_v = my_list[0]
    for i in my_list:
        if max_v < i:
            max_v = i
    return (max_v)
