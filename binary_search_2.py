'''
Binary Search with Duplicates Problem
Find the index of the first occurrence of a key in
a sorted array.
Input: A sorted array of integers
(possibly with duplicates)
and an integer q.
Output: Index of the first occurrence
of q in the array or “−1”
if q does not appear in the array.
'''

def binary_search(keys, query):
    # write your code here
    left = 0
    right = len(keys) - 1
    result = -1
    while right >= left:
        mid = (left + right) // 2
        if keys[mid] == query:
            result = mid
            right = mid - 1
        elif keys[mid] < query:
            left = mid + 1
        else:
            right = mid - 1
    return result


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
