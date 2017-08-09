def getBit(num, index):
    return num & (1 << index) != 0

def setBit(num, index, x): #x is value to set the bit at index to
    mask = 1 << index #make bit at index 1 and everything else 0
    num = num & ~mask #set bit in num at index equal to 0
    if x:
        num = num | mask #if x is 1 set bit to 1 or remain at 0
    return num

def clearBit(num, index):
    mask = 1 << index #create mask to clear at index
    return num & ~mask

def clearBitsMSBthroughI(num, index):
    mask = (1 << index) - 1
    return num & mask

def clearBitsIThrough0(num, i):
    mask = (-1 << (i + 1))
    return num & mask

if __name__ == "__main__":
    result = clearBitsIThrough0(15, 2)
    print(result)
