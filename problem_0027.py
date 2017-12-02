"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Quadratic primes
Problem 27
Euler discovered the remarkable quadratic formula:

n2+n+41n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤390≤n≤39. However, when n=40,40**2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤790≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+bn2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000

where |n| is the modulus/absolute value of nn
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, aa and bb, for the quadratic expression that produces the maximum number of primes for consecutive values of nn, starting with n=0n=0.

Answer:
-59231

Rationale:
Used Miller-Rabin primality test for quickly testing what may be an inefficient
space of possibilities.

References:
[1] http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Proved_correct_up_to_large_N

"""

_known_primes = [2, 3]


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True  # n  is definitely composite


def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(
            _try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(
            _try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])


_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def problem_27(a_range=(-999, 1000), b_range=(-1000, 1001)):
    longest = 0
    answer = None
    for a in range(*a_range):
        for b in range(*b_range):
            c = 0
            n = 0
            f = n ** 2 + a * n + b
            while f > 0 and is_prime(f):
                f = n ** 2 + a * n + b
                c += 1
                n += 1

            if c > longest:
                longest = c
                answer = a * b

    return answer


if __name__ == '__main__':
    print(problem_27())
