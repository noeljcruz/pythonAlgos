'''
Last Digit of Fibonacci Number Problem
Compute the last digit of the n-th Fibonacci
number.
Input: An integer n.
Output: The last digit of the n-th
Fibonacci number.
'''

def fibonacci_last_digit(n):
    if n <= 1:
        return n
    
    fibo_list = [0, 1]

    for i in range(2, 61):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    
    period_place = n % 60
    return fibo_list[period_place] % 10

    return

    # previous = 0
    # current  = 1

    # for _ in range(n - 1):
    #     previous, current = current, previous + current

    # return current % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
