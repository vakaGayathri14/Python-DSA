"""
2.Reverse_a_number

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1
"""

# def reverse_number(n):
#     num = n
#     rev_num = ""
#     while num>0:
#         x = num % 10
#         rev_num = rev_num + str(x)
#         num = num // 10
#     print(rev_num)


# x = int(input("Enter a number : "))
# reverse_number(x)


class Solution:
    def reverse(self, x: int) -> int:
        self.num = x
        negative = self.num < 0
        p = abs(self.num)
        y = ""
        while p > 0:
            z = p % 10
            y = y + str(z)
            p = p // 10
        res = int(y) if y else 0
        res = -res if negative else res
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1
        if res < INT_MIN or res > INT_MAX:
            return 0
        else:
            return res


obj = Solution()
print(obj.reverse(-123))
