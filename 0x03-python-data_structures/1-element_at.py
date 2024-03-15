#!/usr/bin/python

def element_at(my_list, idx):
    if idx > len(my_list) - 1:
        return None
    elif idx == -abs(idx):
        return None
    else:
        return my_list[idx]
