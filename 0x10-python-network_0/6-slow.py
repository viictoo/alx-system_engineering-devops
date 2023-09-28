#!/usr/bin/python3
""" get the max int in a list """

def find_peak(list_of_integers):
    """ method to get the peak """
    if (len(list_of_integers) == 0):
        return None
    peak = list_of_integers[0]
    for i in range(0, len(list_of_integers)):
        if peak < list_of_integers[i]:
            peak = list_of_integers[i]
    return peak
