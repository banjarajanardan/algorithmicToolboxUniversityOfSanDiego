# python3
import sys


def compute_min_refills(distance, tank, stops):
    start = 0
    noOfStops = 0
    stops.append(distance)
    for i in range(len(stops)):
        if (start + tank) >= distance:
            return noOfStops
        for j in range(i, len(stops)):
            if (start + tank) < stops[j]:
                initialstop = start
                start = stops[j-1]
                noOfStops += 1
                finalstop = start
                if initialstop == finalstop:
                    return -1
                break


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    numberOfStops = int(input())
    stops = input()
    stops = list(map(int, stops.split()))
    print(compute_min_refills(d, m, stops))
