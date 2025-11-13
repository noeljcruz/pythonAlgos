'''
Huge Fibonacci Number Problem
Compute the n-th Fibonacci number modulo m.
Input: Integers n and m.
Output: n-th Fibonacci number
modulo m.
'''

def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    modList = [0,1]
    prevMod = 0
    currMod = 1

    for i in range(n - 1):
        tempMod = prevMod
        prevMod = currMod % m
        currMod = (currMod + tempMod) % m
        modList.append(currMod)

        if prevMod == 0 and currMod == 1:
            index = n % (i + 1)
            return modList[index]
    
    return currMod

    # previous = 0
    # current  = 1

    # for _ in range(n - 1):
    #     previous, current = current, previous + current

    # return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
