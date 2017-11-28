"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


Answer:
232792560

Rationale:
you don't need to write any code to solve this problem.
The simplest solution is to multiply all of the largest multiples of the prime factors together:

20 (4 and 5)
19
18 (6 and 3)
17
14 (7 and 2)
13
11

which gives the answer 232792560.
"""
from functools import reduce


def problem_5(*rng):
    n = reduce(lambda x, y: x * y, range(*rng))
    for i in range(20, 1, -1):
        if all(not n / i % j for j in range(*rng)):
            n = n // i
    return n


if __name__ == "__main__":
    print(problem_5(2, 21))
