#Uses python3

import sys

def largest_number(a,n):
    for i in range(n):
        for j in range(n-1):
            if((a[j]+a[j+1])<(a[j+1]+a[j])):
                a[j+1], a[j] = a[j], a[j+1]
    return "".join(a)
    
if __name__ == '__main__':
    n = int(input()) 
    a = input()
    a = a.split()
    print(largest_number(a,n))
    
