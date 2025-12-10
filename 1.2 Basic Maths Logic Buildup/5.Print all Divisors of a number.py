"""
Find the number of factors for a given integer n.

 Examples:

Input: n = 5
Output: 2
Explanation: 5 has 2 factors 1 and 5

Input: n = 25
Output: 3
Explanation: 25 has 3 factors 1, 5, 25

Constraints:
1 ≤ n ≤ 105

"""

# my approach brute force time complexity of the below code is O(N)


class Solution:
    def countFactors(self, n):
        # code here
        num = n
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1
        return count


obj = Solution()
print(obj.countFactors(5))
print(obj.countFactors(25))
print(obj.countFactors(100))


# better solution my approach
class Solution:
    def countFactors(self, n):
        # code here
        num = n
        count = 0
        length = num // 2
        # print(length)
        for i in range(1, length + 1):
            if num % i == 0:
                count = count + 1
        return count + 1


obj = Solution()
print(obj.countFactors(5))
print(obj.countFactors(25))
print(obj.countFactors(100))


# better solution # anirudh's approach timecomplexity is O(N/2) -> further modified as O(N) as O(N) * 1/2, space complexity is O(K)
class Solution:
    def countFactors(self, n):
        # code here
        num = n
        count = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                count = count + 1
        return count + 1


obj = Solution()
print(obj.countFactors(5))
print(obj.countFactors(25))
print(obj.countFactors(100))


# optimal solution #anirudh's approach tc = O(**N)+O(N LOG N), sc = O(K)
from math import sqrt


class Solution:
    def countFactors(self, n):
        # code here
        num = n
        count = 0
        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                count = count + 1
                if num // i != i:
                    count = count + 1
        return count


obj = Solution()
print(obj.countFactors(5))
print(obj.countFactors(25))
print(obj.countFactors(100))
