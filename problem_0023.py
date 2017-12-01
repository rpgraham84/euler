"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


Answer:
4179871

Rationale:
Brute force. Build a set of all the sums of abundant numbers under 28123

"""


DIVISORS = {}


def d(n: int, d=DIVISORS):
    if n in d:
        for i in d[n]:
            yield i
        return

    d[n] = [1]
    yield 1

    for i in range(2, n):
        if not n % i:
            d[n].append(i)
            yield i


def gen_abundant():
    for i in range(1, 28123):
        n = sum(d(i))
        if 28123 > n > i:
            yield i


def problem_23():
    abundant = list(gen_abundant())
    sums = set()
    for a in abundant:
        for b in abundant:
            n = a + b
            if n < 28123:
                sums.add(n)

    return sum(i for i in range(28123) if i not in sums)


if __name__ == '__main__':
    print(problem_23())
