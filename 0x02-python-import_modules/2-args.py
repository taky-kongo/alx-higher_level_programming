#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_args = len(sys.argv) - 1
    if number_args == 0:
        print("0 arguments.")
    elif number_args == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(number_args))
        for args in range(1, number_args + 1):
            print("{}: {}".format(args, sys.argv[args]))
