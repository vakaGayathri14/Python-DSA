"""
Docstring for 1.4 Hashing.Count Frequency in a range

https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

Frequencies in a Limited Array

You are given an array arr[] containing positive integers. The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your have to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).

Examples:

Input: arr[] = [2, 3, 2, 3, 5]
Output: [0, 2, 2, 0, 1]
Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.

Input: arr[] = [3, 3, 3, 3]
Output: [0, 0, 4, 0]
Explanation: We have: 1 occurring 0 times, 2 occurring 0 times, 3 occurring 4 times, and 4 occurring 0 times.

Input: arr[] = [1]
Output: [1]
Explanation: We have: 1 occurring 1 time, and there are no other numbers between 1 and the size of the array.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size()

"""


class Solution:
    def frequencyCount(self, arr):
        #  code here
        my_dict = dict()

        for i in arr:
            my_dict[i] = my_dict.get(i, 0) + 1

        result = []

        for j in range(1, len(arr) + 1):
            result.append(my_dict.get(j, 0))
        return result


obj = Solution()
print(obj.frequencyCount([2, 3, 2, 3, 5]))
