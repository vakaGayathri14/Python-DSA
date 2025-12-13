"""
Docstring for 1.3 Recursion Basics.Recursion problems.2.Print N times with Recursion

https://www.geeksforgeeks.org/problems/print-gfg-n-times/1

Print GFG n times without the loop.

Example:

Input:
5
Output:
GFG GFG GFG GFG GFG

Your Task:
This is a function problem. You only need to complete the function printGfg() that takes N as parameter and prints N times GFG recursively. Don't print newline, it will be added by the driver code.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).

Constraint:
1<=N<=1000

"""


class Solution:
    def printGfg(self, n):
        # Code here
        if n == 0:
            return
        print("GFG", end=" ")
        self.printGfg(n - 1)


obj = Solution()
obj.printGfg(5)
