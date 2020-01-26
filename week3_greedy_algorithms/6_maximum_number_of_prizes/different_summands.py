# Uses python3
# import sys

def optimal_summands(n):
    summands = []
    if n==1:
        summands.append(1)
        return summands
    for i in range(1,n):
        if (n - i)>i:
            summands.append(i)
            n -= i
        else:
            summands.append(n)
            break
    return summands

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
