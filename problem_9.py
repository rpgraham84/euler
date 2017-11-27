"""
Robert Graham (rpgraham84@gmail.com)

Project Euler
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer:
31875000

Rationale:
I started out with the hope that this triple would be primitive and it was.
I could have introduced a 'k' coefficient to each of the terms a,b,c and count
up if needed to check all triples.

Below, I use Euclid's formula for finding primitive triples:

    a=m^2-n^2, b=2mn, c=m^2+n^2
    where m > n > 0

and reduce using the condition a+b+c=1000. So,

    m^2-n^2 + 2mn + m^2+n^2 = 1000

    >    2m^2 + 2mn = 1000

    >   >   m^2 + mn = 500

    >   >   >   m^2 + mn - 500 = 0

That's the condition we check for in the if block while counting up m and n
where m > n > 0.

To derive the values of a, b, and c, from m and n, we use Euclid's definitions
above and return the product abc.
"""


def problem_9():
    # I initially set the range to 1000 to be safe, but m never gets over 20.
    # It takes 20006 iterations to complete. ~20ns
    # a: 375, b: 200, c: 425, m: 20, n: 5
    for m in range(1000):
        for n in range(1000):
            if m > n > 0 and m ** 2 + m * n - 500 == 0:
                a, b, c = (m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2)
                return a * b * c


if __name__ == "__main__":
    print(problem_9())
