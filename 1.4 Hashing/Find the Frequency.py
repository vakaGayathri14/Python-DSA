"""
Docstring for 1.4 Hashing.Find the Frequency

Find the Frequency

Given an array arr of positive integers and an integer x. Return the frequency of x in the array.

Examples :

Input: arr = [1, 1, 1, 1, 1], x = 1
Output: 5
Explanation: Frequency of 1 is 5.

Input: arr = [1, 2, 3, 3, 2, 1], x=2
Output: 2
Explanation: Frequency of 2 is 2.

Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 105
1 <= x <= 105

"""


class Solution:
    def findFrequency(self, arr, x):
        # code here
        my_dict = dict()

        for i in range(0, len(arr)):
            my_dict[arr[i]] = my_dict.get(arr[i], 0) + 1
        return my_dict[x]


obj = Solution()
print(obj.findFrequency([1, 1, 1, 1, 1], 1))


# other approach
class Solution:
    def findFrequency(self, arr, x):
        # code here
        my_dict = dict()

        for i in range(0, len(arr)):
            my_dict[arr[i]] = my_dict.get(arr[i], 0) + 1
        return my_dict.get(x, 0)  # inorder to provide 0 in case of edge case as well


obj = Solution()
print(obj.findFrequency([1, 1, 1, 1, 1], 5))
