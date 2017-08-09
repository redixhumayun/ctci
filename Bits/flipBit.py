import pdb

def flipBit(inputBits):
    array = list(bin(inputBits)[2:])
    valuesArray = [0] * len(array)
    valuesArrayIndex = 0
    firstValue = array[0]
    searchingFor = array[0]
    ctr = 0

    for index, value in enumerate(array):
        # pdb.set_trace()
        if value != searchingFor:
            valuesArray[valuesArrayIndex] = ctr
            valuesArrayIndex += 1
            ctr = 0
            searchingFor = value
        ctr += 1
    #enter the last value
    valuesArray[valuesArrayIndex] = ctr


    return checkSeq(valuesArray, firstValue)

def removeZeroes(array):
    return [value for value in array if value != 0]

def checkSeq(array, firstValue):
    array = removeZeroes(array)
    maximum = 0
    if firstValue == '1':
        for index in range(1, len(array), 2):
            result = array[index - 1] + array[index] + array[index + 1]
            if result > maximum:
                maximum = result
    else:
        for index in range(2, len(array), 2):
            result = array[index - 1] + array[index] + array[index + 1]
            if result > maximum:
                maximum = result
    return maximum



if __name__ == "__main__":
    result = flipBit(1775)
    print(result)
