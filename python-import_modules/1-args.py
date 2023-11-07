#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_slice = sys.argv[1:]
    argv_len = len(arg_slice)
    if argv_len == 0:
        print("{} arguments.".format(argv_len))
    elif argv_len == 1:
        print("{} argument:".format(argv_len))
        print("{}: {}".format(argv_len, arg_slice[0]))
    else:
        print("{} arguments:".format(argv_len))
        for i in range(1, argv_len + 1):
            print("{}: {}".format(i, sys.argv[i]))
