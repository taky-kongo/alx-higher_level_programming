#!/usr/bin/python3
for numb in range(0, 100):
    if numb != 99:
        print("{:02d}".format(numb), end=", ")
    else:
        print("{:d}".format(numb))
