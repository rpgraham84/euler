"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Pandigital multiples
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

Answer:
932718654

Rationale:
is_pandigital checks that
    1. The number passed in has 9 digits
    2. That they are 9 unique digits and
    3. The digits are exactly 1-9

The solution is 9327:
    9327 x 1 = 9327
    9327 x 2 = 18654

    or, 932718654

It is found though brute force search of integers 0 < m < 10,000. Upper limit
found by trial.

"""


def is_pandigital(n: int):
    return len(str(n)) == 9 and len(set(map(int, str(n)))) == 9 and \
           not len(set(map(int, str(n))) - set(range(1, 10)))


def problem_38():
    pandigitals = {}
    for m in range(1, 10_000):
        n = 1
        product = 0
        while len(str(product)) < 9:
            product = int(str(product) + str(m * n))
            if is_pandigital(product):
                pandigitals[(m, n)] = product
            n += 1

    return sorted(pandigitals)[-1]


if __name__ == '__main__':
    print(problem_38())
