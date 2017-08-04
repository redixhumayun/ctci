from random import randint
from bitarray import bitarray

def findDuplicates(arr):
    bitVector = bitarray(32*(2**10))
    for index, num in enumerate(arr):
        if bitVector[num] == False:
            bitVector[num] = True
        else:
            print(num)

def createList():
    arr = []
    for i in range(1000):
        arr.append(randint(0, 32000))
    return arr


if __name__ == "__main__":
    arr = createList()
    findDuplicates(arr)
