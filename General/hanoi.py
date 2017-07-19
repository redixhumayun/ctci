def printMove(fr, to):
    print("move from " + str(fr) + " move to " + str(to))

def Towers(n, fr, to, spare, call):
    print("*******************")
    print("n: ", n)
    print("Call number: ", call)
    print("from: ", fr)
    print("to: ", to)
    print("spare: ", spare)
    # print("Current value of n: ", n)
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to, "first call")
        Towers(1, fr, to, spare, "second call")
        Towers(n-1, spare, to, fr, "third call")

print(Towers(4, 'P1', 'P3', 'P2', "initial call"))
