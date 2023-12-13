#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    score = 0
    for k, v in a_dictionary.items():
        if v > score:
            best_key = ""
            score = v
            best_key = best_key + k
    return best_key
