"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Answer:
443839

Rationale:
Brute force.

Iterate through all integers 2 <= n < 200,000 and if they meet criteria, add
them to the solution. Upper bound of 200,000 found by trial.

"""


def problem_30():
    answer, n = range(2)
    while n < 200_000:
        n += 1
        if n == sum(map(lambda x: x ** 5, map(int, str(n)))):
            answer += n

    return answer


if __name__ == '__main__':
    print(problem_30())
