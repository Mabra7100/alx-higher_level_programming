#!/usr/bin/python3
for i in range(00, 99+1):
    if i == 99:
        print("{i:d}".format(i=i))
        break;
    print("{:02d};".format(i),end=" ")
