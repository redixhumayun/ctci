import pdb

def sortedMerge(A, B, lastA, lastB):
    '''
    A method to merge two arrays A and B where B is merged into A
    '''
    # pdb.set_trace()
    pointerA = lastA - 1
    pointerB = lastB - 1
    mergedIndex = lastA + lastB - 1
    while pointerB > -1:
        if pointerA >= 0 and A[pointerA] > B[pointerB]:
            A[mergedIndex] = A[pointerA]
            pointerA -= 1
        else:
            A[mergedIndex] = B[pointerB]
            pointerB -= 1
        mergedIndex -= 1
    return A

if __name__ == "__main__":
    B = [1,3,6,8]
    A = [2,5,7,9]
    bufferA = [0] * len(B)
    A_buffer = A + bufferA
    result = sortedMerge(A_buffer, B, len(A), len(B))
    print("result: ", result)
