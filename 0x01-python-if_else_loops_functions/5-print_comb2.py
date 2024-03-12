#!/usr/bin/python3
for i in range(0, 99+1):
    if i == 99:
        print("{i:d}".format(i=i))
        break;
    print("{i};".format(i=i),end=" ")
