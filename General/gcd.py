def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    min_num = min(a, b)
    for i in range(min_num, 1, -1):
        if a%i == 0 and b%i == 0:
            return i

result = gcdIter(9, 12)
print(result)
