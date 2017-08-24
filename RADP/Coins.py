import pdb

def Coins(amt, cache):
    '''
    A method to convert denominations in the arr to represent n cents
    '''
    # pdb.set_trace()

    arr = [25, 10, 5, 1] #quarter, dime, nickel, penny. Need to stop reinitializing this every call
    result = 0

    if amt < 0:
        return 0 #base case

    if cache[amt] != 0:
        return cache[amt]

    if amt == 0:
        return 1 #base case

    for i in arr:
        result += Coins(amt - i, cache)

    cache[amt] = result

    return result


if __name__ == "__main__":
    n = 10
    result = Coins(n, [0]*(n+1))
    print(result)
