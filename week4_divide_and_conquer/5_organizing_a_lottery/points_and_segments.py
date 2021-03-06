# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    start_points = zip(starts, ['l'] * len(starts), range(len(starts)))
    end_points = zip(ends, ['r'] * len(ends), range(len(ends)))
    point_points = zip(points, ['p'] * len(points), range(len(points)))

    sort_list = chain(start_points, end_points, point_points)
    sort_list = sorted(sort_list, key=lambda a: (a[0], a[1]))
    segment = 0
    i = 0
    for num, letter, index in sort_list:
        if letter == 'l':
            segment += 1
        elif letter == 'r':
            segment -= 1
        else:
            cnt[index] = segment
            i += 1
    return cnt

if __name__ == '__main__':

    a = input()
    n, m = map(int, a.split())
    data = list(map(int, a.split()))
    starts =[]
    ends =[]
    for i in range(n):
        temp1, temp2 = map(int, input().split())
        starts.append(temp1)
        ends.append(temp2)
    points = list(map(int, input().split()))

    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
