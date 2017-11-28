"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer: 25164150

Rationale: This one is so simple it shouldn't really be #6
"""


def problem_6():
    return sum(range(1, 101)) ** 2 - sum(x ** 2 for x in range(1, 101))


if __name__ == "__main__":
    print(problem_6())
