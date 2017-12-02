"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Answer:
45228

Rationale:
Iterate through each possible permutation of the digits 1 through 9 and check
for the 1st digit times the next 4 digits equals the last 4 digits and check
for the 1st and 2nd digits times the next 3 digits equal to the last 4 digits.

For each case that matches, add the answer to the set of products. Finally,
return the set of products.

Uses the next_permutation algorithm from problem 24.

"""
from math import factorial


def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return True


def problem_32(digits=list(range(1, 10))):
    products = set()
    for i in range(factorial(len(digits))):
        # for the number of possible permutations, 9!
        a = int("".join(map(str, digits[:2])))
        b = int("".join(map(str, digits[2:5])))
        c = int("".join(map(str, digits[-4:])))
        if a * b == c:
            products.add(int("".join(map(str, digits[-4:]))))

        a = int("".join(map(str, digits[:1])))
        b = int("".join(map(str, digits[1:5])))
        if a * b == c:
            products.add(int("".join(map(str, digits[-4:]))))

        next_permutation(digits)

    return sum(products)


if __name__ == '__main__':
    print(problem_32())
