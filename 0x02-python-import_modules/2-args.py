#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = len(sys.argv) - 1
    print("{} argument".format(num), end='')
    if num > 1:
        print("s:")
        for i in range(num):
            print("{}: {}".format((i + 1), sys.argv[i + 1]))
    elif num == 1:
        print(":\n1: {}".format(sys.argv[1]))
    else:
        print("s.")


