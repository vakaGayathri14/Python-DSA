"""
Docstring for 1.3 Recursion Basics.Recursion problems.7.Check if String is palindrome

Palindrome String
You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

Examples :

Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.

Input: s = "abc"
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.

Constraints:
1 ≤ s.size() ≤ 106
The string s contains only lowercase english letters (a-z).
"""


# approach 1
class Solution:
    def isPalindrome(self, s):
        # code here
        s1 = s.lower()
        return s1 == s1[::-1]


obj = Solution()
print(obj.isPalindrome("abba"))
print(obj.isPalindrome("abc"))

# best approach


class Solution:
    def isPalindrome(self, s, left, right):
        if left >= right:
            return True

        if s[left] != s[right]:
            return False

        return self.isPalindrome(s, left + 1, right - 1)


obj = Solution()
print(obj.isPalindrome("abba", 0, 3))
print(obj.isPalindrome("abc", 0, 2))
