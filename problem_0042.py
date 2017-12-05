"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Coded triangle numbers
Problem 42
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

Answer:
162

Rationale:
This algorithm first checks to see what the max word value is for all of the
words. This number is used as the maximum value of triangle number that will
be needed to check to see if a word is triangular or not.

The main function returns a sum of a list with a 1 for every triangular word in
the set of words. This counts the total number of triangular words.

runtime: 7ms average

"""
from string import ascii_uppercase


def value_of(word: str):
    return sum(ascii_uppercase.index(c) + 1 for c in word.upper())


def problem_42():
    with open("p042_words.txt") as f:
        words = [s.replace("\"", "") for s in f.read().split(",")]

    n, triangles = 0, []
    triangle = n * (n + 1) // 2
    max_word = max(value_of(word) for word in words)
    while triangle < max_word:
        triangles.append(n * (n + 1) // 2)
        n += 1
        triangle = n * (n + 1) // 2

    return sum(1 for word in words if value_of(word) in triangles)


if __name__ == '__main__':
    print(problem_42())
