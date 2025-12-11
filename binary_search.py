'''
Sorted Array Search Problem
Search a key in a sorted array of keys.
Input: A sorted array K[0] < K[1] <
· · · < K[n−1] of distinct integers and
an integer q.
Output: Check whether q occurs
in the array.
'''

def binary_search(keys, query):
    # write your code here
    left = 0
    right = len(keys) - 1
    while right >= left:
        mid = (left + right) // 2
        if keys[mid] == query:
            return mid
        elif keys[mid] < query:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
