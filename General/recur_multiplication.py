def recur(a, b):
    print("a: ", a)
    print("b: ", b)
    if a == 0:
        return 0
    elif a == 1:
        return b
    else:
        return b + recur(a - 1, b)


result = recur(5, 4)
print(result)
