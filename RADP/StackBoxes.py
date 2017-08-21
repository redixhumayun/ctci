import collections
import pdb

class Box():
    '''
    A class to create box objects. Each will have height, width and depth
    '''
    def __init__(self, h, w, d):
        self.height = h
        self.width = w
        self.depth = d

def canBeAbove(box, bottomBox):
    if bottomBox.height > box.height and bottomBox.width > box.width and bottomBox.depth > box.depth:
        return True
    else:
        return False

def createStack2(boxesArray, bottomIndex):
    bottom = boxesArray[bottomIndex]
    maxHeight = 0
    for i in range(1, len(boxesArray)):
        if canBeAbove(boxesArray[i], bottom):
            height = createStack2(boxesArray, i)
            maxHeight = max(maxHeight, height)

    maxHeight += bottom.height
    return maxHeight

def createStack(arrayOfBoxes):
    #sort by height in descending order
    # pdb.set_trace()
    newArray = sorted(arrayOfBoxes, key=lambda box: box.height, reverse=True)
    print(newArray)
    maxHeight = 0
    for index, obj in enumerate(newArray):
        height = createStack2(newArray, index)
        maxHeight = max(height, maxHeight)
    return maxHeight

if __name__ == "__main__":
    Box = collections.namedtuple('Box', 'height width depth')
    box1 = Box(height=5, width=10, depth=10)
    box2 = Box(height=6, width=8, depth=10)
    box3 = Box(height=9.5, width=12, depth=15)
    box4 = Box(height=12, width=15, depth=12)
    box5 = Box(height=11.5, width=12.5, depth=11)

    Boxes = [box1, box2, box3, box4, box5]
    BoxesObjectArray = []

    for box in Boxes:
        BoxesObjectArray.append(Box(box.height, box.width, box.depth))
    value = createStack(BoxesObjectArray)
    print(value)
