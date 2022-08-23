#!/usr/bin/python3
for i in range(0, 8):
    start = i + 1
    for j in range(start, 10):
        if i != j:
            print("{}{}".format(i, j), end=', ')
print("{}{}".format(i + 1, i + 2))
