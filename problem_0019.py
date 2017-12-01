"""
Robert Graham (rpgraham84@gmail.com)
Project Euler

Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Answer:
171

Rationale:
Python to the rescue again.

"""
import datetime


def problem_19():
    d = datetime.datetime(1901, 1, 1)
    count = 0
    while d.year < 2001:
        if d.weekday() == 6 and d.day == 1:
            count += 1
        d += datetime.timedelta(days=1)

    return count


if __name__ == '__main__':
    print(problem_19())
