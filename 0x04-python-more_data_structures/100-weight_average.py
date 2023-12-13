#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    weight, score, average = 0, 0, 0
    for i in range(len(my_list)):
        weight = weight + my_list[i][1]
        score = score + (my_list[i][0] * my_list[i][1])
    average = score / weight
    return average
