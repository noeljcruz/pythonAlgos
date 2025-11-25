'''
Maximum Product of Two Sequences Problem
Find the maximum dot product of two sequences
of numbers.
Input: Two sequences of n positive
integers: price1, . . . ,pricen
and clicks1, . . . , clicksn.
Output: The maximum value
of price1 · c1 + · · · + pricen
· cn,
where c1, . . . , cn is a permutation
of clicks1, . . . , clicksn.
'''

from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    max_product = 0

    # for permutation in permutations(second_sequence):
    #     dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
    #     max_product = max(max_product, dot_product)

    first_sequence.sort()
    second_sequence.sort()
    max_product = sum(
        first_sequence[i] * second_sequence[i] 
        for i in range(len(first_sequence)))

    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
