import pdb

def mergeSort(input_arr):
    # pdb.set_trace()
    if len(input_arr) <= 1:
        return input_arr
    middle = len(input_arr) // 2
    left = input_arr[:middle]
    right = input_arr[middle:]
    leftArr = mergeSort(left)
    rightArr = mergeSort(right)
    return merge(leftArr, rightArr)

def merge(left, right):
    output_arr = []
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output_arr.append(left[i])
            i += 1
        else:
            output_arr.append(right[j])
            j += 1
    while i < len(left):
        output_arr.append(left[i])
        i += 1
    while j < len(right):
        output_arr.append(right[j])
        j += 1
    return output_arr

if __name__ == "__main__":
    arr = [4,6,2,1,8,9]
    result = mergeSort(arr)
    print(result)
