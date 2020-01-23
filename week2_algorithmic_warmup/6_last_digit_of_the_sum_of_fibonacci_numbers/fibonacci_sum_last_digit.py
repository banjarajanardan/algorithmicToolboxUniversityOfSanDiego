# Uses python3
import sys

def periodic(m):
    a = 0
    b = 1
    c = a+b
    for i in range(m*m):
        c = (a+b)%m
        a, b = b, c
        if (a == 0 and b ==1):
            return (i+1)

def solve(n, m):
    rem = n % periodic(m)

    first =  0
    second = 1
    res = rem

    for i in range(1, rem):
        res = (first + second) % m
        first, second = second, res

    return (res%m)

def fibonacciSumLastDigit(n):
    lastDigitOfNPlus2 = solve(n+2, 10)
    lastDigitOf2 = solve(2, 10)
    if (lastDigitOfNPlus2 >= lastDigitOf2):
        return (lastDigitOfNPlus2 - lastDigitOf2)
    else:
        return ((10 + lastDigitOfNPlus2) - lastDigitOf2)

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacciSumLastDigit(n))
