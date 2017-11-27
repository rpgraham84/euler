"""
Project Euler

Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Solution:
The largest prime factor can be no larger than the
square root of 600851475143. So, we need to test all the
primes up to sqrt(600851475143), about 775146.

The sieve could takes less than 1MB of memory because this number is
relatively small.

"""
import sys
from math import sqrt, floor
from itertools import count


class InvalidArguments(TypeError):
    pass


def sieve_of_eratosthenes(limit: int):
    sqrt_of_limit = int(sqrt(limit))
    sieve = [True] * limit
    for i in range(2, sqrt_of_limit):
        if sieve[i]:
            for j in (i**2 + c * i for c in range(limit)):
                if j >= limit:
                    break

                sieve[j] = False

    return [index for index, e in enumerate(sieve) if e][2:]


def segmented_sieve(limit: int):
    offset = blocksize = int(sqrt(limit))
    primes = sieve_of_eratosthenes(blocksize)
    yield primes


def solution(n: int):
    return segmented_sieve(n)


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2
        number = int(sys.argv[1])
    except (AssertionError, ValueError):
        number = 600851475143

    print(solution(number))

