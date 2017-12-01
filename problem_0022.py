"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Answer:
871198282

Rationale:
Brute force.

"""
from string import ascii_uppercase


with open("p022_names.txt") as f:
    t = f.read()


names = sorted(map(lambda x: x.replace("\"", ""), t.split(',')))


def name_letter_value(name: str):
    return sum(ascii_uppercase.index(c) + 1 for c in name.upper())


def problem_22():
    s = 0
    for i, name in enumerate(names):
        s += (i + 1) * name_letter_value(name)

    return s


if __name__ == '__main__':
    print(problem_22())
