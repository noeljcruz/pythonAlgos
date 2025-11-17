'''
Maximizing the Value of the Loot Problem
Find the maximal value of items that fit into the
backpack.
Input: The capacity of a backpack
W as well as the weights
(w1, . . . ,wn) and costs (c1, . . . , cn) of
n different compounds.
Output: The maximum total
value of fractions of items that fit
into the backpack of the given capacity:
i.e., the maximum value
of c1 · f1 + · · · + cn · fn such that
w1·f1+· · ·+wn·fn ≤W and 0 ≤ fi ≤
1 for all i (fi is the fraction of the
i-th item taken to the backpack).
'''

from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    perUnitList = []
    capacityRemaining = capacity
    weightsList = list(weights)
    valuesList = list(values)

    for i in range(len(valuesList)):
        perUnit = valuesList[i] / weightsList[i]
        perUnitList.append(perUnit)

    while capacityRemaining > 0 and len(perUnitList) > 0:
        mostValIndex = perUnitList.index(max(perUnitList))

        if capacityRemaining >= weightsList[mostValIndex]:
            value += valuesList[mostValIndex]
            capacityRemaining -= weightsList[mostValIndex]
            perUnitList.remove(perUnitList[mostValIndex])
            weightsList.remove(weightsList[mostValIndex])
            valuesList.remove(valuesList[mostValIndex])
        else:
            # value += (perUnitList[mostValIndex] * capacityRemaining)
            value += valuesList[mostValIndex] * (capacityRemaining / weightsList[mostValIndex])
            capacityRemaining = 0


    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
