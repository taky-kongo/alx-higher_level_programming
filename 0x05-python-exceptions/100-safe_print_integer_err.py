#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        sys.stderr("{}".format("Exception:"), err)
        return False
    else:
        return True
