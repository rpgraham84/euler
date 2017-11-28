"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Longest Collatz sequence
Problem 14 
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Answer:


Rationale:


"""


def gen_collatz(n: int):
    while n > 100000:
        yield n
        if n % 2:
            n = 3 * n + 1
        else:
            n = n // 2
    yield 1


def problem_14():
    longest = (0, 0)
    for i in range(1, 1000000):
        l = len(list(gen_collatz(i)))
        if l > longest[0]:
            longest = (l, i)

    return longest[1]


if __name__ == '__main__':
    print(problem_14())
