'''
Fibonacci Number Problem
Compute the n-th Fibonacci number.
Input: An integer n.
Output: n-th Fibonacci number.
'''

def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
