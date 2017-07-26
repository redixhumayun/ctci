#! /usr/bin/env python3
import pdb

def findMagicIndex(arr):
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if arr[midpoint] == midpoint:
            found = True
            return arr[midpoint]
        else:
            if arr[midpoint] > midpoint:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return False


if __name__ == "__main__":
    index = findMagicIndex([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13])
    print(index)
