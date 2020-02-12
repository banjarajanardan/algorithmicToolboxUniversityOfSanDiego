# Uses python3
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    k = r
    i = l

    while i <= r:
        if a[i] < x:
            a[j], a[i] = a[i], a[j]
            j += 1
            i += 1
        elif a[i] > x:
            a[i], a[r] = a[r], a[i]
            r -= 1
        else:
            i += 1
            
    return j, r


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)


if __name__ == '__main__':
    n = int(input())    
    a = input()
    a = list(map(int, a.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
