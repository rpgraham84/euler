"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Maximum path sum II
Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

Answer:
7273

Rationale:
Solved with the dynamic programming solution from problem 18.

"""


with open("p067_triangle.txt") as f:
    t = f.read()


TRIANGLE = list(map(str.split, t.split('\n')))


for i, row in enumerate(TRIANGLE):
    TRIANGLE[i] = list(map(int, row))


def problem_67(triangle=TRIANGLE):
    for i, row in enumerate(triangle[::-1]):
        above_index = -1 * (i + 2)
        if abs(above_index) <= len(triangle):
            row_above = triangle[above_index]
            for idx, ele in enumerate(row[:-1]):
                next_ele = row[idx + 1]
                row_above[idx] = max(row_above[idx] + ele,
                                     row_above[idx] + next_ele)

    return triangle[0][0]


if __name__ == '__main__':
    print(problem_67())
