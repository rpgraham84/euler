"""
Project Euler

Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer:
6857

Rationale:
I revisited this problem after solving 12 using the factor_tree[1] and thought
this would be a good use case for the same method. This finds the first (and
largest) prime factor in the factor tree.

References:
[1] https://www.quora.com/How-do-you-make-a-factor-tree-of-an-integer-e-g-12-or-180

"""
import re


r = re.compile(r'\((\d+), N')


def factor_tree(n: int):
    for i in range(2, n):
        if n % i == 0:
            return n, factor_tree(n // i), factor_tree(i)
    return n, None, None


def problem_3(n=600851475143):
    return int(r.findall(str(factor_tree(n)))[0])

if __name__ == "__main__":
    print(problem_3())

