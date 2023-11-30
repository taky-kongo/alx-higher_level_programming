#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_args = len(sys.argv) - 1
    result = 0
    if number_args == 0:
        print("0")
    elif number_args == 1:
        print("{}".format(sys.argv[1]))
    else:
        for i in range(1, number_args + 1):
            result = result + int(sys.argv[i])
        print(result)
