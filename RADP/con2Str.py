def convertToString(num):
    result = ''
    if num < 10:
        return str(num)
    else:
        rem = num % 10
        num = num // 10
        result += convertToString(num) + convertToString(rem)
    return result


if __name__ == "__main__":
    num = 123456789
    result = convertToString(num)
    print(result)
    print(type(result))
