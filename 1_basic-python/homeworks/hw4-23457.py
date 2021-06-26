import random
random.seed(123)

# Вспомогательная функция для генерирования списков

def randomlist(minlen, maxlen, minnum, maxnum):
    listlen = random.randint(minlen, maxlen)
    return [random.randrange(minnum, maxnum) for i in range(listlen)]
    
# Task 2

list0 = randomlist(10, 20, 1, 100)
print(f"Исходный список: {list0}")

list1 = [list0[i] for i in range(1, len(list0)) if list0[i] > list0[i-1]]
print(f"Отфильтрованный список: {list1}")

# Task 3

div_20_21 = [i for i in range(20,241) if i % 20 == 0 or i % 21 == 0]

# Task 4

listWithRepeats = randomlist(15, 15, 1, 10)
listWithoutRepeats = [i for i in listWithRepeats if listWithRepeats.count(i) == 1]

# Task 5

from functools import reduce
targetList = [i for i in range(100, 1001) if i % 2 == 0]
result = reduce(lambda a, b: a * b, targetList)

# Task 7

from functools import reduce # it was imported in task 5, but now task 7 can run independently

def fact(base):
    for i in range(1, base+1):
        yield reduce(lambda x, y: x * y, range(1, i+1))

# but is a generator really faster in this case?..

def fact2(base):
    cache = [1]
    print(cache[-1])
    for i in range(2, base + 1):
        cache.append(cache[-1] * i)
        print(cache[-1])
        
from time import perf_counter

tic = perf_counter()
for i in fact(1500):
    print(i)
toc = perf_counter()

tic2 = perf_counter()
fact2(1500)
toc2 = perf_counter()

print("Runtime 1: {}".format(toc-tic))
print("Runtime 2: {}".format(toc2-tic2))

# Runtime will get progressively worse with larger numbers as the generator can't store values in memory and has to recalculate everything
# A list, on the other hand, can be used to cache the previously calculated numbers