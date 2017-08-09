def bin2str(dec):
    value = int(str(dec - int(dec))[2:])
    if value / (2**32) >= 2:
        raise ValueError("Can't fit inside 32 bits")
    binList = [0] * 33
    initialDivisor = 32
    while value > 1:
        newValue = value % (2 ** initialDivisor)
        if newValue < value:
            value = newValue
            binList[initialDivisor] = 1
        initialDivisor -= 1
    return list(reversed(binList))

if __name__ == '__main__':
    result = bin2str(0.78)
    print(''.join(str(n) for n in result))
