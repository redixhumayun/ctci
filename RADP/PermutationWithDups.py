def findFrequencyTable(string):
    '''
    A method to find the frequency of character occurences
    using a hash table
    '''
    hashTable = {}
    for char in string:
        if char in hashTable:
            hashTable[char] += 1
        else:
            hashTable[char] = 1

    return hashTable

def permuteString(hashTable, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix)
        return
    else:
        for key, value in hashTable.items():
            count = value
            if count > 0:
                hashTable[key] = hashTable[key] - 1
                permuteString(hashTable, prefix + key, remaining - 1, result)
                hashTable[key] = count
    return result

if __name__ == "__main__":
    string = 'AAB'
    hashTable = findFrequencyTable(string)
    result = []
    result = permuteString(hashTable, "", len(string), result)
    print(result)
