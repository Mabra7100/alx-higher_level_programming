#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{i}{j}".format(i=i, j=j))
            break
        print("{i}{j}".format(i=i, j=j), end=", ")
