import pdb
import sys

def minimumAbsoluteDifference(n, arr):
    arr = sorted(arr)

    minimum = sys.maxsize
    for i in range(0, n-1, 1):
        if abs(arr[i] - arr[i+1]) < minimum:
            minimum = abs(arr[i] - arr[i+1])
    return minimum


if __name__ == "__main__":
    n = 7
    arr = [-3,5,2,1,0,3,6]
    result = minimumAbsoluteDifference(n, arr)
    assert result == 0
