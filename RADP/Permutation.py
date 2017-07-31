#! /usr/bin/env python3
import pdb

def Permutation(string):
    '''
    A function that will create permutations of a string
    Return type: None
    '''
    # pdb.set_trace()
    #base case for recursion
    if len(string) == 1:
        return string

    result = [] #empty results array

    #iterating through string here
    for i in range(len(string)):
        perms = Permutation(string[:i] + string[i+1:])
        remainingChar = string[i]
        for perm in perms:
            result.append(remainingChar + perm)
    return result


if __name__ == "__main__":
    result = Permutation('ABC')
    print(result)
