"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Answer:
648

Rationale:
Python is like not even coding.

"""
from math import factorial as f


def problem_20():
    sum(map(int, str(f(100))))


if __name__ == '__main__':
    print(problem_20())
