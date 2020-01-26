# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda segment: segment.end)
    current = segments[0].end
    points.append(current)
    for i in segments:
        if(current<i.start or current>i.end):
            current = i.end
            points.append(current)
    return points

if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        a, b = map(int, input().split())
        data.append(a)
        data.append(b)
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=" ")