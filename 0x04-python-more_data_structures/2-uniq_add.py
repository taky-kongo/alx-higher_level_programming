#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == []:
        return 0
    from functools import reduce
    result = (reduce(lambda x, y: x + y, list(set(my_list))))
    return result
