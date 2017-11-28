"""
Project Euler

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Answer:
906609

Rationale:
The largest combination of 3 digit numbers is 999x999 = 998001.
That means the largest possible palindromic number must be the first one
smaller than that, 997799. Our generator starts there and counts down
palindromic numbers in order, 996699, 995599, and so on.

Then, each palindromic number is divided by every 3 digit number from 999-100
in descending order. If there is no remainder in the division and if the
length of the whole part of the division is 3 digits long, then that is our answer.
It will be the largest because we began from the largest possible palindromic
number that meets criteria (being composed of two 3-digit numbers).
"""


def problem_4():
    # Palindromic num gen starting from 997799 counting down
    for n in (int(f'{b}{str(b)[::-1]}') for b in range(997, 99, -1)):
        for i in range(999, 99, -1):
            if not n % i and len(str(n // i)) == 3:
                return n


if __name__ == "__main__":
    print(problem_4())
