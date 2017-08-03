def rotated(arr, elemToFind):
    for i in range(len(arr)):
        # if arr[i+1] > arr[i] and arr[i] != elemToFind:
        #     pass
        # else:
        #     #found pivot point. Element has to be to the right
        #     return binarySearch(arr, i, elemToFind)
        if arr[i] == elemToFind:
            return i
        elif arr[i+1] < arr[i]:
            return binarySearch(arr, i, elemToFind)


def binarySearch(arr, index, elemToFind):
    low = index
    high = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if elemToFind < arr[mid]:
            high = mid - 1
        elif elemToFind > arr[mid]:
            low = mid + 1
        else:
            return mid

if __name__ == "__main__":
    arr = [15,16,19,20,25,1,3,4,5,7,7,10,14]
    result = rotated(arr, 7)
    print(result)
