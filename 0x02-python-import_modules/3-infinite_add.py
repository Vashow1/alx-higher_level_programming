#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    num = len(args) - 1
    sum = 0
    if num > 0:
        for i in range(num):
            sum = sum + int(args[i + 1])
    print(sum)
