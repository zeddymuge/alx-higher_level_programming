#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        x = list(a_dictionary())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[x]:
                x = key
        return x
    return None
