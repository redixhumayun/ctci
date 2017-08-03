def anagramSort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = anagramSort(arr[:middle])
    right = anagramSort(arr[middle:])
    return merge(left, right)

def merge(left, right):
    output = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        leftElem = ''.join(sorted(left[i])).strip()
        rightElem = ''.join(sorted(right[j])).strip()
        if leftElem <= rightElem:
            output.append(leftElem)
            i += 1
        else:
            output.append(rightElem)
            j += 1
    while i < len(left):
        leftElem = ''.join(sorted(left[i])).strip()
        output.append(leftElem)
    while j < len(right):
        rightElem = ''.join(sorted(right[j])).strip()
        output.append(rightElem)
    return output


    return output


if __name__ == "__main__":
    arr = ['debit card', 'listen', 'bad credit', 'silent', 'dormitory', 'dirty room']
    result = anagramSort(arr)
    print(result)
