#!/usr/bin/python3
import sys

num_args = len(sys.argv)
count = 1
print("{} arguments:".format(num_args - 1))
for arg in sys.argv[1:]:
    print("{}: {}".format(count, arg))
    count += 1
