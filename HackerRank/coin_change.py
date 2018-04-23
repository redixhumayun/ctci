def coin_change_abstraction(amount, coin_list):
    coin_cache = [[0 for coin in coin_list]for i in range(amount + 1)]
    return coin_change(amount, coin_list, 0, coin_cache)


def coin_change(amount, coin_list, index, coin_cache):
    #amount is the total amount
    #coin_list is the list of denominations
    #index is the current pointer in the coin_list
    if index > len(coin_list) - 1:
        return 0
    if coin_cache[amount][index] > 0:
        return coin_cache[amount][index]
    if index >= len(coin_list) - 1 and amount % coin_list[index] == 0:
        return 1

    ways = 0
    denomAmount = coin_list[index]
    i = 0
    while (i * denomAmount) <= amount:
        newAmount = amount - (i * denomAmount)
        ways += coin_change(newAmount, coin_list, index + 1, coin_cache)
        i += 1
    coin_cache[amount][index] = ways
    return ways

if __name__ == "__main__":
    amount = 10
    coin_list = [5,2,3,6]
    sorted(coin_list).reverse()
    result = coin_change_abstraction(amount, coin_list)
    print(result)
