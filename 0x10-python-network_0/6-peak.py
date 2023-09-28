#!/usr/bin/python3
""" get the max int in a list """


def find_peak(list_of_integers):
    """ method to get the peak """
    if (len(list_of_integers) == 0):
        return None
    ll = 0
    rr = len(list_of_integers) - 1
    
    while ll < rr:
        ml = (ll + rr) // 2

        if list_of_integers[ml] < list_of_integers[rr]:
            ll = ml + 1
        else:
            rr = ml
    return list_of_integers[ll]
