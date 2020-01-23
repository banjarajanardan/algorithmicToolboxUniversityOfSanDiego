# Uses python3

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

if __name__ == '__main__':
    n = int(input())
    print((solve(n+1,10)*solve(n,10))%10)
