import urllib.request

def goodland(n, k, arr):
    total = 0
    i = 0
    last = 0
    while i < n:
        total += 1
        j = i + (k-1)
        if j > n:
            j = n-1
        while last <= j < n and arr[j] == 0:
            j -= 1
        if j < last: #not possible because no power plant in range
            return -1
        #otherwise a 1 has been found at some index
        last = j + 1 #doing this to keep it k non-inclusive
        j += k
        i = j
    return total


if __name__ == "__main__":
    link = "https://hr-testcases-us-east-1.s3.amazonaws.com/21552/input15.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1503578098&Signature=7R2c3mnpm2jntdoUp9t2iutKw5A%3D&response-content-type=text%2Fplain"
    with urllib.request.urlopen(link) as data:
        firstLine = 0
        for line in data:
            if firstLine == 0:
                n, k = map(int, line.split())
                firstLine += 1
            else:
                arr = list(map(int, line.split()))
    result = goodland(n, k, arr)
    # n = 6
    # k = 2
    # arr = [0,1,1,1,1,0]
    # result = goodland(n, k, arr)
    # print(result)
