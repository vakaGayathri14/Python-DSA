"""
Docstring for 2. Different types of Sorting.3.Insertion Sort
Insertion Sort
Difficulty: EasyAccuracy: 66.61%Submissions: 262K+Points: 2Average Time: 15m
Given an array arr[] of positive integers.The task is to complete the insertsort() function which is used to implement Insertion Sort.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: The sorted array will be [1, 3, 4, 7, 9].

Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Explanation: The sorted array will be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

Input: arr[] = [4, 1, 9]
Output: [1, 4, 9]
Explanation: The sorted array will be [1, 4, 9].

Constraints:
1 ≤ arr.size() ≤ 1000
1 ≤ arr[i] ≤ 1000

"""


# Please change the array in-place
class Solution:
    def insertionSort(self, arr):
        # Start from the second element; first element is a sorted sub-array of length 1
        for i in range(1, len(arr)):
            key = arr[i]  # element we want to insert
            j = i - 1  # index that scans the sorted part (left side)

            # Shift larger elements one step to the right
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            # Place 'key' into its correct spot
            arr[j + 1] = key

        return arr


obj = Solution()
print(obj.insertionSort([4, 1, 3, 9, 7]))
