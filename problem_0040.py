"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Champernowne's constant
Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

Answer:
210

Rationale:
Brute force search for the digits

"""
from functools import reduce


def gen_digits():
    c = "1"
    a = 2
    for n in range(7):
        while len(c) < 10 ** n:
            c += str(a)
            a += 1
            if len(c) > 10 ** n:
                yield int(c[10 ** n - 1])
                continue


def problem_40():
    return reduce(lambda x, y: x * y, gen_digits())


if __name__ == '__main__':
    print(problem_40())