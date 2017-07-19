def karatsuba(x, y):
    if x < 10 or y < 10:
        return x*y

    #making the two numbers strings here
    str_x = str(x)
    str_y = str(y)

    #finding the mid point for each number here
    n = max(len(str(x)), len(str(y)))
    n_2 = int(n / 2)

    print("*********")
    print("x: ", x)
    print("y: ", y)
    print("n_2: ", n_2)
    print("*********")

    #higher bits of each number
    x_h = int(str_x[:-n_2])
    y_h = int(str_y[:-n_2])

    #lower bits for each number here
    x_l = int(str_x[-n_2:])
    y_l = int(str_y[-n_2:])

    print("X_h: ", x_h)
    print("X_l: ", x_l)
    print("Y_h: ", y_h)
    print("Y_l: ", y_l)

    a = karatsuba(x_h, y_h)
    d = karatsuba(x_l, y_l)

    print('------------')
    print("X_H: ", x_h)
    print("X_L: ", x_l)
    print("Y_H: ", y_h)
    print("Y_L: ", y_l)
    print('------------')

    print("a: ", a)
    print("d: ", d)



    e = karatsuba(x_h + x_l, y_h + y_l) - a - d

    return a*10**(2*n_2) + e*10**(n_2) + d





result = karatsuba(1234, 8765)
print(result)
