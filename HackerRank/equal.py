import pdb

def equal(chocolates, ctr, arr):
    # pdb.set_trace()
    if checkEqual(chocolates) <= 1:
        return ctr
    min_value = min(chocolates)
    max_value = max(chocolates)
    max_index = chocolates.index(max_value)
    result = 0
    for num in [n for n in arr if n <= (max_value - min_value)]:
        chocolates[max_index] = max_value - num
        return equal(chocolates, ctr + 1, arr)


def checkEqual(chocolates):
    return len(set(chocolates))


if __name__ == "__main__":
    chocolates = [2,2,3,7]
    arr = [1,2,5]
    arr.reverse()
    result = equal(chocolates, 0, arr)
    print(result)
