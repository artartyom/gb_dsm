# task 6-a

# uses provided arguments as starting and breaking points

from itertools import count
from sys import argv

startNum, maxNum = map(int, argv[1:])

for i in count(startNum):
    print(i)
    if i == maxNum:
        break