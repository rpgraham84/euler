"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

Answer:
840

Rationale:
This algorithm first iterates through 1-1000 inclusive and builds the primitive
pythagorean triples using Euclid's algorithm. Its similar to problem 9, but
generalized to search for solutions for a given int, i
Then, the multiples of primitives are added to the set as long as their sum isn't
greater than 1000. The longest set of solutions found is checked and updated
each iteration of a primitive triple.

I tried to use sets, but python doesn't like when you modify them during
iteration of them.

840's triples:
{(56, 390, 394),
 (105, 360, 375),
 (120, 350, 370),
 (140, 336, 364),
 (168, 315, 357),
 (210, 280, 350),
 (240, 252, 348)}


"""
from collections import defaultdict


def prime_pythagorean_triple(i: int):
    for m in range(10):
        for n in range(10):
            if m > n > 0 and m * n + m ** 2 == i / 2:
                a, b, c = (m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2)
                return a, b, c


def problem_39():
    triples = defaultdict(list)
    for i in range(1001):
        sol = prime_pythagorean_triple(i)
        if sol:
            triples[i].append(tuple(sorted(sol)))
        else:
            triples[i] = list()

    longest = (0, 0)
    for n, solutions in triples.items():
        for solution in solutions:
            for k in range(2, 1000):
                multiple = tuple(sorted(map(lambda x: k * x, solution)))
                if not len(solution) or sum(multiple) > 1000:
                    break

                triples[sum(multiple)].append(multiple)
            longest = max(longest, (len(set(triples[n])), n))

    return longest[1]


if __name__ == '__main__':
    print(problem_39())
