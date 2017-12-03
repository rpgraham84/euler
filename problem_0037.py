"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Answer:
748317

Rationale:
For each 'p' in 'primes', the function 'truncate' is used to
generate the set of possible truncations in both directions. If the set of p's
truncations minus the set of primes is empty (that is, if all the truncations
of p are prime), and p > 10 then p is added into the final sum.

Truncatable primes:
[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]

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


def truncate(n: int):
    left = set(int(str(n)[i:]) for i in range(len(str(n))))
    right = set(int(str(n)[:i]) for i in range(len(str(n))) if i)
    left.update(right)
    return left


def problem_37():
    primes = set(sieve_of_eratosthenes(1_000_000))
    return sum(p for p in primes if p > 10 and not len(truncate(p) - primes))

if __name__ == '__main__':
    print(problem_37())

