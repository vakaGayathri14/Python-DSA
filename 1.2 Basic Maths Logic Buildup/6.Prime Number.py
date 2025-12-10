"""
Given a number n, determine whether it is a prime number or not.
Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Examples :

Input: n = 7
Output: true
Explanation: 7 has exactly two divisors: 1 and 7, making it a prime number.

Input: n = 25
Output: false
Explanation: 25 has more than two divisors: 1, 5, and 25, so it is not a prime number.

Input: n = 1
Output: false
Explanation: 1 has only one divisor (1 itself), which is not sufficient for it to be considered prime.

Constraints:
1 ≤ n ≤ 109
"""


# my approach
class Solution:
    def isPrime(self, n):
        # code here
        num = n
        factors = 0

        for i in range(1, num + 1):
            if num % i == 0:
                factors = factors + 1
        return factors == 2


obj = Solution()
print(obj.isPrime(1))
print(obj.isPrime(25))
print(obj.isPrime(7))
print(obj.isPrime(0))
print(obj.isPrime(-3))

# other approach


class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False

        factors = 0

        for i in range(1, n + 1):
            if n % i == 0:
                factors += 1

            # If more than 2 factors, no need to continue → not prime
            if factors > 2:
                return False

        return factors == 2
