import pdb

def pairwise(num):
    # pdb.set_trace()
    length = len(list(bin(num)))
    index = 0
    while index < length:
        first = getBit(num, index)
        second = getBit(num, index + 1)
        if (first ^ second):
            #bits are different
            if(first):
                num += (1 << index)
            else:
                num -= (1 << index)
        index += 2
    return num

def getBit(num, index):
    return num & (1 << index) != 0


if __name__ == "__main__":
    result = pairwise(5)
    print(result)
