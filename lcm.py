'''
Least Common Multiple Problem
Compute the least common multiple of two positive
integers.
Input: Two positive integers a
and b.
Output: The least common multiple
of a and b.
'''

def lcm(a, b):

    num1 = a
    num2 = b
    if num1 == num2:
        return num1
    
    if b > a:
        a, b = b, a
    curr_gcd = 1
    gcdList = [1]

    while curr_gcd > 0:
        curr_gcd = a % b
        a = b
        b = curr_gcd
        # if curr_gcd > 0: 
        gcdList.append(a)
    
    index = -1
    curr_lcm = int((num1  * num2) / gcdList[index])

    while curr_lcm < num1 or curr_lcm < num2:
        index = index -1
        curr_lcm = int((num1 * num2) / gcdList[index])

    # if gcdList[index] == 1:
    #     return max(num1, num2)
    # else:
    
    return curr_lcm

    # for l in range(1, a * b + 1):
    #     if l % a == 0 and l % b == 0:
    #         return l

    # assert False

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

