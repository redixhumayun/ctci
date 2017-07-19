#!python3

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    print("Left: ", left)
    print("Right: ", right)

    return merge(left, right)

def merge(a, b):
    print("***********")
    print("a: ", a)
    print("b: ", b)
    result = []
    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result += a[i:]
    result += b[j:]
    print("Result: ", result)
    return result

final = merge_sort([4,2,1,5,3,7])
