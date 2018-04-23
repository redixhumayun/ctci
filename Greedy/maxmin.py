import sys

def maxmin(n, k, arr):
    arr = sorted(arr)
    maximum = 0
    minimum = 0
    minDiff = sys.maxsize
    for i in range(0, n-k+1):
        minimum = arr[i]
        maximum = arr[i+(k-1)]
        diff = maximum - minimum
        if diff < minDiff:
            minDiff = diff
    return minDiff

if __name__ == "__main__":
    n = 7
    k = 3
    arr = [100,200,300,350,400,401,402]
    result = maxmin(n, k, arr)
    print(result)
    assert result == 2
