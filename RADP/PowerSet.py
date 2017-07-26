#! /usr/bin/env python3
import pdb

def findSubsets(inputSet):
    '''
    A method to return a list of all subsets that can be obtained from the
    input set
    Return Type: list<int>
    '''
    # pdb.set_trace()
    if inputSet == []:
        return []
    returnSets = [inputSet]
    for i in range(0, len(inputSet)):
        items = findSubsets(inputSet[:i] + inputSet[i+1:])
        for subset in items:
            if subset not in returnSets:
                returnSets.append(subset)
    return returnSets

if __name__ == "__main__":
    arr = [1,2, 3, 4, 5]
    result = findSubsets(arr)
    print(result)
