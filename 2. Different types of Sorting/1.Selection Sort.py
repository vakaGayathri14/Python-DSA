"""
Docstring for 2. Different types of Sorting.1.Selection Sort

https://www.geeksforgeeks.org/problems/selection-sort/1

Selection Sort

Given an array arr, use selection sort to sort arr[] in increasing order.

Examples :

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: Maintain sorted (in bold) and unsorted subarrays. Select 1. Array becomes 1 4 3 9 7. Select 3. Array becomes 1 3 4 9 7. Select 4. Array becomes 1 3 4 9 7. Select 7. Array becomes 1 3 4 7 9. Select 9. Array becomes 1 3 4 7 9.

Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Input: arr[] = [38, 31, 20, 14, 30]
Output: [14, 20, 30, 31, 38]

Constraints:
1 ≤ arr.size() ≤ 103
1 ≤ arr[i] ≤ 106

"""

# ascending order


class Solution:
    def selectionSort(self, arr):
        # code here
        n = len(arr)

        for i in range(0, n):
            min_index = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


obj = Solution()
print(obj.selectionSort([4, 1, 3, 9, 7]))


# descending order


class Solution:
    def selectionSort(self, arr):
        # code here
        n = len(arr)

        for i in range(0, n):
            max_index = i

            for j in range(i + 1, n):
                if arr[j] > arr[max_index]:
                    max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]
        return arr


obj = Solution()
print(obj.selectionSort([4, 1, 3, 9, 7]))
