import pdb

def Coins(coinValueList, change, minCoins):
    pdb.set_trace()
    for cents in range(1, change+1):
        count = cents
        for value in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-value] + 1 < count:
                count = minCoins[cents-value] + 1
        minCoins[cents-value] = count
    return minCoins[change]


if __name__ == "__main__":
    coinValueList = [1,5,10,25];
    change = 11;
    minCoins = [0,1,2,3,4,1,2,3,4,5,1]
    result = Coins(coinValueList, change, minCoins);
    print(result)
