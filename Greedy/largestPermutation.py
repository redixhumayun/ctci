def largestPermutation(n, k, arr):
    index = 0
    while k > 0 and index < len(arr):
        if arr[index] != n - index:
            swapIndex = findNum(n-index, arr)
            arr[index], arr[swapIndex] = arr[swapIndex], arr[index]
            k -= 1
        index += 1
    return arr

def findNum(num, arr):
    for index, value in enumerate(arr):
        if value == num:
            return index


if __name__ == "__main__":
    n = 5
    k = 2
    arr = [3,4,2,5,1]
    result = largestPermutation(n, k, arr)
    for num in result:
        print(str(num) + ' ', end='')
    print('\n')
