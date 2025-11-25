'''
Car Fueling Problem
Compute the minimum number of gas tank refills
to get from one city to another.
Input: Integers d and m, as well
as a sequence of integers stop1 <
stop2 < · · · < stopn.
Output: The minimum number
of refills to get from one city
to another if a car can travel
at most m miles on a full tank.
The distance between the cities is
d miles and there are gas stations
at distances stop1,stop2, . . . ,stopn
along the way. We assume that
a car starts with a full tank.
'''

from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    refills = 0
    stopsList = list(stops)
    stopsList.insert(0, 0)
    stopsList.append(distance)
    fullTank = tank

    if tank >= distance:
        return 0
    
    for i in range(len(stopsList) - 1):
        distToNext = stopsList[i + 1] - stopsList[i]
        if tank >= distToNext:
            tank -= distToNext
        else:
            refills += 1
            tank = fullTank - distToNext
            if tank < 0:
                return -1

    return refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
