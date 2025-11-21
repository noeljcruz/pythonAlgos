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
    value = 0.0
    # write your code here
    items = []

    for v, w in zip(values, weights):
        if w <= 0:
            continue
        items.append((v, w, v/w))
    items.sort(key=lambda x: x[2], reverse=True)

    for v, w, ratio in items:
        if capacity == 0:
            break
        take = min(w, capacity)
        value += ratio * take
        capacity -= take

    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
