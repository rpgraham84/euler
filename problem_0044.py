"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Pentagon numbers
Problem 44
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

Answer:
5482660


Rationale:
The key to solving this problem is to reverse the function for generating 
pentagonal numbers into a function that determines whether or not a number is
pentagonal. If you take the function given and solve for n:

                         p = (3 * n - 1)n / 2
              (3 * n - 1)n = 2 * p
             3 * n ^ 2 - n = 2 * p
             n ^ 2 - n / 3 = 2 * p / 3
    n ^ 2 - n / 3 + 1 / 36 = 2 * p / 3 + 1 / 36
           (n - 1 / 6) ^ 2 = 2 * p / 3 + 1 / 36
                 n - 1 / 6 = sqrt(2 * p / 3 + 1 / 36)
                         n = sqrt(2 * p / 3 + 1 / 36) + 1 / 6

In order for n to be an index into the set of pentagonal numbers, it must be
whole. Therefore, we check that our inverse function returns an integer and if
so, then p is pentagonal.

Armed with this function, we can walk through the pentagonal numbers and test
whether any two meet the requirements. Because the solution is counting up,
the first pair of pentagonals found that meet criteria will be the ones with
the smallest difference, D, between them.
"""
from math import sqrt


def is_pentagonal(p: int):
    return (sqrt(2 * p / 3 + 1 / 36) + 1 / 6).is_integer()


def pentagon(n: int):
    return n * (3 * n - 1) // 2


def problem_44():
    pk_n = 0
    while True:
        for pj_n in range(1, pk_n):
            pk, pj = pentagon(pk_n), pentagon(pj_n)
            if is_pentagonal(pk + pj) and is_pentagonal(pk - pj):
                return pk - pj

        pk_n += 1


if __name__ == '__main__':
    print(problem_44())
