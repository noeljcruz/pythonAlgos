'''
Money Change Problem
Compute the minimum number of coins needed
to change the given value into coins with denominations
1, 5, and 10.
Input: An integer money.
Output: The minimum number
of coins with denominations 1, 5,
and 10 that changes money.
'''

def change(money):
    # write your code here

    money = money
    count = 0

    while money > 0:
        if money >= 10:
            money -= 10
            count += 1
        elif money >= 5:
            money -= 5
            count += 1
        elif money >= 1:
            money -= 1
            count += 1

    return count


if __name__ == '__main__':
    m = int(input())
    print(change(m))
