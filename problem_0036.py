"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Double-base palindromes
Problem 36
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

Answer:
872187

Rationale:


"""


def double_base_palindrome(n: int):
    if str(n)[::-1] == str(n) and bin(n)[2:][::-1] == bin(n)[2:]:
        return True

    return False


def problem_36():
    return sum(i for i in range(1, 1_000_000) if double_base_palindrome(i))


if __name__ == '__main__':
    print(problem_36())
