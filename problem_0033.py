"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Digit cancelling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

Answer:
100

Rationale:
Brute force search.

16/64
19/95
26/65
49/98

"""
from fractions import Fraction as F


def problem_33():
    answer = F(1, 1)
    for n in range(10, 100):
        for d in range(10, 100):
            for digit in map(int, str(n)):
                new_n = str(n).replace(str(digit), '')
                new_d = str(d).replace(str(digit), '')
                if all((digit, new_n, new_d, str(digit) in str(d))) and int(new_d):
                    if F(n, d) == F(int(new_n), int(new_d)) and d > n:
                        answer *= F(n, d)

    return answer.denominator


if __name__ == '__main__':
    print(problem_33())
