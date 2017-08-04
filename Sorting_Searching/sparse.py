import pdb
import timeit

def sparse(string_arr, value):
    '''
    A method to search an array of strings to look for value
    '''
    # pdb.set_trace()
    first = 0
    last = len(string_arr) - 1
    mid = (first + last) // 2
    while first <= last:
        if string_arr[mid] == '':
            mid += 1
        else:
            if value < string_arr[mid]:
                last = mid - 1
                mid = (first + last) // 2
            elif value > string_arr[mid]:
                first = mid + 1
                mid = (first + last) // 2
            else:
                return mid
    return -1

def binary_search():
    SETUP_CODE = '''
from __main__ import sparse
    '''
    TEST_CODE = '''
arr = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
value = 'ball'
sparse(arr, value)
    '''
    print(timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=1000))


if __name__ == "__main__":
    binary_search()
