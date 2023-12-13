#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    score = 0
    for k, v in a_dictionary.items():
        best_key = ""
        if v > score:
            score = v
            best_key = best_key + k
    return best_key
