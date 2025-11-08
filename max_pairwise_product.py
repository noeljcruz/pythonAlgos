'''
Maximum Pairwise Product Problem
Find the maximum product of two distinct numbers
in a sequence of non-negative integers.
Input: An integer n and a sequence
of n non-negative integers.
Output: The maximum value
that can be obtained by multiplying
two different elements from
the sequence.
'''

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    
    '''
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])
    '''

    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
