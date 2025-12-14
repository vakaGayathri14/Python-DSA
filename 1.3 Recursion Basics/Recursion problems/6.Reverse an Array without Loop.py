"""
Docstring for 1.3 Recursion Basics.Recursion problems.6.Reverse an Array without Loop

https://www.geeksforgeeks.org/problems/reverse-sub-array5620/1

Reverse sub array

Given an array arr, you need to reverse a subarray of that array. The range of this subarray is given by indices l and r (1-based indexing).

Examples:

Input: arr[] = [1, 2, 3, 4, 5, 6, 7], l = 2, r = 4
Output: [1, 4, 3, 2, 5, 6, 7]
Explanation: After reversing the elements in range 2 to 4 (2, 3, 4), modified array is 1, 4, 3, 2, 5, 6, 7.

Input: arr[] = [1, 6, 7, 4], l = 1, r = 4
Output: [4, 7, 6, 1]
Explanation: After reversing the elements in range 1 to 4 (1, 6, 7, 4), modified array is 4, 7, 6, 1.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ l ≤ r ≤ arr.size()

"""


class Solution:
    def reverseSubArray(self, arr, l, r):
        # base case (1-based indexing)
        if l >= r:
            return arr

        # swap using 1-based index
        arr[l - 1], arr[r - 1] = arr[r - 1], arr[l - 1]

        return self.reverseSubArray(arr, l + 1, r - 1)


obj = Solution()
print(obj.reverseSubArray([1, 2, 3, 4, 5, 6, 7], 2, 4))
print(obj.reverseSubArray([1, 6, 7, 4], 1, 4))
