"""
Docstring for 1.3 Recursion Basics.Recursion problems.5.Factorial of N numbers

https://www.geeksforgeeks.org/problems/factorial5739/1

Factorial
Given a positive integer, n. Find the factorial of n.

Examples :

Input: n = 5
Output: 120
Explanation: 1 x 2 x 3 x 4 x 5 = 120

Input: n = 4
Output: 24
Explanation: 1 x 2 x 3 x 4 = 24

Constraints:
0 ≤ n ≤ 12

"""


class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        # code here
        if n == 1:
            return 1

        return n * self.factorial(n - 1)


obj = Solution()
print(obj.factorial(5))
print(obj.factorial(4))
