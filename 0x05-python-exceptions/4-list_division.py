#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_result = list()
    try:
        for i in range(list_length):
            try:
                list_result.append(my_list_1[i] / my_list_2[i])
            except TypeError:
                list_result.append(0)
                print("wrong type")
            except ZeroDivisionError:
                list_result.append(0)
                print("division by 0")
            except IndexError:
                list_result.append(0)
                print("out of range")
    finally:
        return list_result
