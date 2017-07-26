#! /usr/bin/env python3

def fibonacci(n, cache):
    '''
    A method to return the nth fibonacci number
    Return type: int
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if cache[n] == 0:
        cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]

if __name__ == "__main__":
    n = 25
    result = fibonacci(n, [0] * (n+1))
    print(result)
