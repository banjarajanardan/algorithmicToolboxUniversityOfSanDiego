# Uses python3
import sys

def get_change(m):
    tens = m//10
    m = m - tens*10
    fives = m//5
    m = m - fives*5
    return (tens + fives + m)

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
