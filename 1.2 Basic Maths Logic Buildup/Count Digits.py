"""
Problem statement
Ninja want to add coding to his skill set so he started learning it. On the first day, he stuck to a problem in which he has given a long integer ‘X’ and had to count the number of digits in it.

Ninja called you for help as you are his only friend. Help him to solve the problem.

EXAMPLE:
Input: 'X' = 2

Output: 1

As only one digit is ‘2’ present in ‘X’ so answer is ‘1’.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= 'T' <= 1000
1 <= ‘X’ <= 10^18
Time Limit: 1 sec
Sample Input 1 :
2
89
870
Sample Output 1 :
2
3
Explanation Of Sample Input 1 :
In test case ‘1’. There are ‘2’ digits present in ‘89’ that is ‘8’ and ‘9’. So the answer is ‘2’.
In test case ‘2’. There are ‘3’ digits present in ‘870’ that is ‘8’, ‘7’ and ‘0’. So the answer is ‘3’.
Sample Input 2 :
2
240
1
Sample Output 2 :
3
1

"""


def countDigit(n: int) -> int:
    num = n
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count


x = int(input("Enter a number : "))
print(countDigit(x))
