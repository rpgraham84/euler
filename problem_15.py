"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

Answer:
137846528820

Rationale:
The total number of lattice paths[1] for a square is given as 2n Combination n

Combination function borrowed from stack overflow[2].

References:
[1] https://en.wikipedia.org/wiki/Lattice_path#Problems_and_proofs
[2] https://stackoverflow.com/a/3027128

"""
from operator import mul
from fractions import Fraction
from functools import reduce


def nCk(n: int, k: int):
    return int(reduce(mul, (Fraction(n - i, i + 1) for i in range(k)), 1))


def problem_15(n=20):
    return nCk(n * 2, n)

if __name__ == '__main__':
    print(problem_15())
