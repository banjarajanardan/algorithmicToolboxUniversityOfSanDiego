# Uses python3

def calc_fib(f, n):
    if (n <= 1):
        return n

    f[0] = 0
    f[1] = 1
    for i in range(2,n+1):
        f[i] = (f[i-2] + f[i-1])%10
    return f

def findLastDigit(n): 
    f = [0] * 61; 

    f = calc_fib(f, 60); 
  
    return f[n % 60]; 

n = int(input())
print(findLastDigit(n))
