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

    max_index1 = -1
    max_index2 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]: 
            max_index1 = i

    for j in range(n):
        if j != max_index1 and max_index2 == -1 or numbers[j] > numbers[max_index2]:
            max_index2 = j
    
    '''
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])
    '''

    return numbers[max_index1] * numbers[max_index2]


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
