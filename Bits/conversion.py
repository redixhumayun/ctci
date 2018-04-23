def conversion(int1, int2):
    bitDiffCounter = 0 #counter for different bits
    larger = int1 if int1 > int2 else int2
    smaller = int2 if int1 > int2 else int1
    while larger != 0 and smaller != 0:
        if getLastBit(larger) != getLastBit(smaller):
            bitDiffCounter += 1
        larger = larger >> 1 #shift one bit to the right for int1
        smaller = smaller >> 1 #shift one bit to the right for int2

    while larger != 0:
        bitDiffCounter += 1
        larger = larger >> 1

    return bitDiffCounter

def getLastBit(num):
    return (num & 1) != 0

if __name__ == "__main__":
    result = conversion(3, 5)
    print(result)
