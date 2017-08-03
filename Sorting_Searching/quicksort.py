import pdb

def quicksort(arr, left, right):
    pdb.set_trace()
    index = partition(arr, left, right)
    if left < index - 1:
        quicksort(arr, left, index - 1)
    if index < right:
        quicksort(arr, index, right)

def partition(arr, left, right):
    pivot = arr[(left + right) // 2] #picking the median element as pivot
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <=right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1

    return left

if __name__ == '__main__':
    arr = [4,6,2,1,8,9]
    quicksort(arr, 0, 5)
