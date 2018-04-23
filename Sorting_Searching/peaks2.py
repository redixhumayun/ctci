import sys
import pdb

def findPeaksAndValleys(array):
    # pdb.set_trace()
    for i in range(1, len(array), 2):
        bigIndex = findMax(array, i - 1, i , i + 1)
        if bigIndex != i:
            array[i], array[bigIndex] = array[bigIndex], array[i]
    return array

def findMax(array, a, b, c):
    aValue = array[a] if a >= 0 and a < len(array) else -sys.maxsize-1
    bValue = array[b] if b >= 0 and b < len(array) else -sys.maxsize-1
    cValue = array[c] if c >= 0 and c < len(array) else -sys.maxsize-1

    maximum = max(aValue, max(bValue, cValue))
    if maximum == aValue:
        return a
    elif maximum == bValue:
        return b
    else:
        return c


if __name__ == "__main__":
    array = [5,3,1,2,3]
    result = findPeaksAndValleys(array)
    print(result)
