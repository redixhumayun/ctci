import pdb

def nextNum(integer):
    large = nextLargestNumber(integer)
    small = nextSmallestNumber(integer)
    print(large, small)

def nextLargestNumber(integer):
    # pdb.set_trace()
    num = integer
    p = 0
    c0 = 0
    c1 = 0
    #checking number of zeros
    while (num & 1) == 0 and num != 0:
        num = num >> 1
        c0 += 1

    while (num & 1) == 1:
        c1 += 1
        num = num >> 1

    #get position p
    p = c0 + c1

    #clearing all bits to the right of p
    integer = integer | 1 << p
    a = 1 << p
    a = a - 1
    mask = ~a
    integer = integer & mask

    #adding back all but one 1s to the right of p at rightmost indexes
    mask = (1 << (c1-1)) - 1
    integer = integer | mask

    return integer

def nextSmallestNumber(integer):
    p = 0
    num = integer
    c0 = 0
    c1 = 0

    while (num & 1) == 1:
        num = num >> 1
        c1 += 1

    while (num & 1) == 0 and num != 0:
        num = num >> 1
        c0 += 1

    #Shifting the 1 to 0 at position p
    p = c0 + c1
    integer = integer ^ (1 << p)

    #Clear all bits to the right of p
    a = (1 << p) - 1
    mask = ~a
    integer = integer & mask

    #Insert (c1+1) 1s to the right of p
    mask = ((c1 + 1) << 1) - 1
    mask = mask << (c0-1)
    integer = integer | mask

    return integer

if __name__ == "__main__":
    nextNum(12)
