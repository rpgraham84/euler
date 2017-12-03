"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Answer:
55

Rationale:
I spent a lot of time solving the wrong problem here before I realized what a
circular prime is, but I finally got it.

This algorithm first finds all the primes under 1,000,000 and then tests all of
the circular rotations of the base 10 digits for primality. If so, it is added
to the set of circular primes and then

"""


def sieve_of_eratosthenes(limit: int):
    sqrt_of_limit = int(limit ** 0.5)
    sieve = [True] * limit
    for i in range(2, sqrt_of_limit):
        if sieve[i]:
            for j in (i**2 + c * i for c in range(limit)):
                if j >= limit:
                    break

                sieve[j] = False

    return [index for index, e in enumerate(sieve) if e][2:]


def get_cycles(n):
    return set(int(str(n)[i:] + str(n)[:i]) for i in range(len(str(n))) if i)


def problem_35():
    primes = set(sieve_of_eratosthenes(1_000_000))
    circulars = set()
    for prime in primes:
        if not len(get_cycles(prime) - primes):
            circulars.add(prime)

    return len(circulars)


if __name__ == '__main__':
    print(problem_35())
