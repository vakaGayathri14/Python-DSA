"""
Docstring for 1.3 Recursion Basics.Recursion problems.4.Sum of first N natural numbers without Loop

https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1

Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

Examples:

Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225

Input: n = 7
Output: 784
Explanation: 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784

Constraints:
1 <= n <= 200

"""


class Solution:
    def sumOfSeries(self, n):
        # code here
        if n == 1:
            return 1
        return n**3 + self.sumOfSeries(n - 1)


obj = Solution()
print(obj.sumOfSeries(5))
print(obj.sumOfSeries(7))
