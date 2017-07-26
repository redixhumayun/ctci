#! /usr/bin/env python3
import pdb

def tripleStep(num, cache):
    '''
    A function to count number of possible ways to climb steps
    Return type: int
    '''
    # pdb.set_trace()
    possibleSteps = [3,2,1]
    if num < 0:
        return 0
    if num == 0:
        return 1
    if cache[num] > -1:
        return cache[num]
    cache[num] = tripleStep(num - 3, cache) + tripleStep(num - 2, cache) + tripleStep(num - 1, cache)
    return cache[num]

if __name__ == "__main__":
    num = 52
    cache = [-1] * (num + 1)
    result = tripleStep(num, cache)
    print(result)
