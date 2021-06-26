# Task 1

from sys import argv

workhours, salary, bonus = map(float, argv[1:])

print(f"Заработная плата: {workhours * salary + bonus}")