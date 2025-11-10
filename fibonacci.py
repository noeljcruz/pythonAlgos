'''
Fibonacci Number Problem
Compute the n-th Fibonacci number.
Input: An integer n.
Output: n-th Fibonacci number.
'''

def fibonacci_number(n):
    if n <= 1:
        return n
    
    fibo_list = [0, 1]

    for i in range(2, n+1):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

    return fibo_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
