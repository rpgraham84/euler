"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Answer:
31626

Rationale:
Brute force. Attempted using Euler's generalization but prime checking was too
difficult for this problem.

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


def gen_amicable():
    for a in range(1, 10000):
        b = sum(d(a))
        if sum(d(b)) == a and a != b:
            yield a
            yield b


def problem_21():
    return sum(set(gen_amicable()))


if __name__ == '__main__':
    print(problem_21())
