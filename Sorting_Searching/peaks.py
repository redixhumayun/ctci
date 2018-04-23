import pdb

def peaks(array, start, end):
    # pdb.set_trace()
    if start > end:
        return
    lastElem = array.pop()
    array.insert(start, lastElem)
    peaks(array, start + 2, end - 1)
    return array

def quickSort(array, left, right):
    index = partition(array, left, right)
    if left < index - 1:
        quickSort(array, left, index - 1)
    if right > index:
        quickSort(array, index, right)

def partition(array, left, right):
    pivot = array[(left+right) // 2]
    while left <= right:
        while array[right] > pivot:
            right -= 1
        while array[left] < pivot:
            left += 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left

if __name__ == "__main__":
    array = [5,8,6,2,3,4,6]
    quickSort(array, 0, len(array) - 1)
    result = peaks(array, 0, len(array) - 1)
    print(result)
