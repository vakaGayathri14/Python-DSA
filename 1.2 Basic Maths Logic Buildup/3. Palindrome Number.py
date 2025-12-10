"""
Docstring for 1.2 Basic Maths Logic Buildup.3. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-2**31 <= x <= 2**31 - 1


Follow up: Could you solve it without converting the integer to a string?

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        self.num = x
        res = 0
        while self.num > 0:
            ld = self.num % 10
            res = (res * 10) + ld
            self.num //= 10
        return res == x


obj = Solution()
print(obj.isPalindrome(1234))
print(obj.isPalindrome(101))
