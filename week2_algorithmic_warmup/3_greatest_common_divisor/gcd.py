# Uses python3
import sys
def gcd_naive(a, b):
    if b > a:
        a,b = b,a
    if b==0:
        return a
    else:
        rem = a%b
        return gcd_naive(b,rem)

    return current_gcd

if __name__ == "__main__":
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
