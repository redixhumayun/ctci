def insertion(N, M, i, j):
    mask1 = (-1 << (j+1))
    mask2 = ((1 << i) - 1)
    mask = mask1 | mask2
    N_cleared = N & mask
    M_shifted = M << i
    return (N_cleared | M_shifted)

if __name__ == "__main__":
    N = int('10000000000', 2)
    M = int('10011', 2)
    result = insertion(N, M, 2, 6)
    print(bin(result))
