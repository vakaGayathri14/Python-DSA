"""
Docstring for 1.3 Recursion Basics.Recursion problems.1.Print 1 to N without Loop

https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1

You are given an integer n. You have  to print all numbers from 1 to n.
Note: You must use recursion only, and print all numbers from 1 to n in a single line, separated by spaces.

Examples:

Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10

Input: n = 5
Output: 1 2 3 4 5

Input: n = 1
Output: 1

Constraints:
1 ≤ n ≤ 103

"""


class Solution:
    def printNos(self, n):
        # Code here
        if n == 0:
            return
        self.printNos(n - 1)
        print(n, end=" ")


obj = Solution()
obj.printNos(4)
