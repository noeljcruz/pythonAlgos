'''
Greatest Common Divisor Problem
Compute the greatest common divisor of two
positive integers.
Input: Two positive integers a
and b.
Output: The greatest common divisor
of a and b.
'''

def gcd(a, b):

    if b > a:
        a, b = b, a
    current_gcd = 1

    while current_gcd > 0:
        current_gcd = a % b
        a = b
        b = current_gcd

    return a

    # for d in range(2, min(a, b) + 1):
    #     if a % d == 0 and b % d == 0:
    #         if d > current_gcd:
    #             current_gcd = d

    # return current_gcd


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
