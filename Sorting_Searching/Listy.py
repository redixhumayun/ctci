import pdb

class Listy():
    def __init__(self):
        self.elements = [1,3,6,8,9,12]

    def elementAt(self, i):
        try:
            return self.elements[i]
        except IndexError:
            return -1

    def findLastElement(self, value):
        index = 1
        elem = self.elementAt(index)
        while elem != -1 and elem < value:
            if index == 1:
                index = index * 2
            else:
                index = index ** 2
            elem = self.elementAt(index)
        return index


def findElement(value):
    # pdb.set_trace()
    listy = Listy()
    lastIndex = listy.findLastElement(value)
    index = lastIndex // 2
    return binarySearch(value, index, lastIndex, listy)


def binarySearch(value, first, last, listy):
    while first <= last:
        mid = (first + last) // 2
        if listy.elementAt(mid) < value:
            first = mid + 1
        elif listy.elementAt(mid) > value:
            last = mid - 1
        else:
            return mid




if __name__ == "__main__":
    result = findElement(6)
    print(result)
