#! /usr/bin/env python3
import pdb

def RecursiveMul(a, b):
    '''
    A method to multiply two numbers without using *
    '''
    # pdb.set_trace()
    result = 0
    if a == 0 or b == 0:
        return 0
    if a == 1 or b == 1:
        # return multiply(a, b)
        return max(a, b)
    else:
        if a >= b:
            result += RecursiveMul(a - 1, b) + RecursiveMul(1, b)
        elif a < b:
            result += RecursiveMul(a, b - 1) + RecursiveMul(a, 1)
    return result

def multiply(a, b):
    arr = [[1 for y in range(b)] for x in range(a)]
    sum_result = 0
    for row in arr:
        for elem in row:
            sum_result += elem
    return sum_result

if __name__ == "__main__":
    result = RecursiveMul(10, 12)
    print(result)
