#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = 0
    for i in set(my_list):
        uniq += i
    return (uniq)
