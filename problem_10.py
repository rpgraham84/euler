"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer:
142913828922

Rationale:
Yawn.

"""
from math import sqrt


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


def problem_10():
    return sum(sieve_of_eratosthenes(2000000))


if __name__ == "__main__":
    print(problem_10())
