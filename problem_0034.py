"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Answer:
40730

Rationale:
Brute force search for integers less than 50,000. Upper bound discovered by
trial.

"""
from math import factorial as f


def problem_34():
    return sum(n for n in range(10, 50_000) if n == sum(map(lambda x: f(int(x)), str(n))))


if __name__ == '__main__':
    print(problem_34())
