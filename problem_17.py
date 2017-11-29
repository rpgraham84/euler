"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Answer:
21124

Rationale:
Brute force.

"""

TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}
TEENS = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
ONES = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}


def get_hundreds(n: int):
    if n < 100:
        return ""

    conjunction = ""
    if n % 100:
        conjunction = "and"

    return f'{get_ones(int(str(n)[0]))} hundred {conjunction}'


def get_tens(n: int):
    if n < 10 or int(str(n)[-2]) == 0:
        return ""

    if int(str(n)[-2]) == 1:
        return TEENS[int(str(n)[-2:])]

    return TENS[int(str(n)[-2])]


def get_ones(n: int):
    digit = int(str(n)[-1])
    if not digit or (n > 9 and int(str(n)[-2]) == 1):
        return ""

    return ONES[digit]


def to_words(n: int):
    if n == 1000:
        return "one thousand"

    return f'{get_hundreds(n)} {get_tens(n)} {get_ones(n)}'.strip()


def problem_17():
    return sum(len(to_words(n).replace(" ", "")) for n in range(1, 1001))


if __name__ == '__main__':
    print(problem_17())
