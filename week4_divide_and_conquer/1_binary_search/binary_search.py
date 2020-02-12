# Uses python3
import sys

def binary_search(data, x, left, right):
    while(left<=right):
        index = left + int((right - left)/2)
        if x==data[index]:
            return index
        if x<data[index]:
            right = index-1
        elif x>data[index]:
            left = index+1
    return -1

if __name__ == '__main__':
    n, *data = map(int,input().split())
    m, *keys = map(int,input().split())
    left, right = 0, len(data)-1
    for x in keys:
        print(binary_search(data, x, left, right), end=" ")
