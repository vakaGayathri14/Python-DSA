"""
Docstring for 1.2 Basic Maths Logic Buildup.4.Armstrong Numbers

1.0 https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1

You are given a 3-digit number n, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371.

Examples:

Input: n = 153
Output: true
Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153.

Input: n = 372
Output: false
Explanation: 372 is not an Armstrong number since 33 + 73 + 23 = 378.

Input: n = 100
Output: false
Explanation: 100 is not an Armstrong number since 13 + 03 + 03 = 1.

Constraints:
100 ≤ n <1000
"""


class Solution:
    def armstrongNumber(self, n):
        # code here
        num = n
        res = 0
        while num > 0:
            last_digit = num % 10
            res = res + last_digit**3
            num //= 10
        return n == res


obj = Solution()
print(obj.armstrongNumber(371))


# 2.# https://takeuforward.org/plus/dsa/problems/check-if-the-number-if-armstrong

"""
Check if the Number is Armstrong

You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.

An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.


Examples:
Input: n = 153

Output: true

Explanation: Number of digits : 3.

13 + 53 + 33 = 1 + 125 + 27 = 153.

Therefore, it is an Armstrong number.

Input: n = 12

Output: false

Explanation: Number of digits : 2.

12 + 22 = 1 + 4 = 5.

Therefore, it is not an Armstrong number.

"""


class Solution:
    def isArmstrong(self, n):
        num = n
        res = 0
        while num > 0:
            last_digit = num % 10
            res = res + last_digit ** len(str(num))
            num //= 10
        return res == n


obj = Solution()
print(obj.isArmstrong(371))
