#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_key = []
    for k, v in a_dictionary.items():
        if value == v:
            list_key.append(k)
    for i in list_key:
        del a_dictionary[i]
    return a_dictionary
