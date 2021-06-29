# Task 1

line = input("Введите текст. Пустая строка завершит операцию. ")

with open("hw5-1_out.txt", "w", encoding="utf-8") as target:
    while line != "":
        target.write(line + "\n")
        line = input("Введите следующую строку. Пустая строка завершит операцию. ")
        
# Task 2

with open("hw5-2_in.txt", "r", encoding="utf-8") as source:
    splitlines = map(str.split, source.readlines())
    
wordcounts = [len(line) for line in splitlines]
print("Всего {} строк.".format(len(wordcounts)))

for i, j in enumerate(wordcounts):
    print("Строка {}: {} слов.".format(i+1, j))
    
# Task 3

with open("hw5-3_in.txt", "r", encoding="utf-8") as source:
    splitlines = list(map(lambda x: x.strip().split(), source.readlines()))
    
poorPeople = []
total = 0
poorTotal = 0

for person in splitlines:
    if int(person[1]) < 20000: 
        poorPeople.append(person[0])
        poorTotal += int(person[1])
    total += int(person[1])
    
print("Эти сотрудники имеют оклад менее 20 тысяч: {}.".format(", ".join(poorPeople)))
print("Их средний оклад составляет {}.".format(round(poorTotal / len(poorPeople), 2)))
print("При этом средний оклад по компании составляет {}.".format(round(total / len(splitlines), 2)))
print("Так что может создаваться впечатление, что все сотрудники очень хорошо зарабатывают!")

# Task 4

dictEnRu = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

source = open("hw5-4_in.txt", "r", encoding = "utf-8")
target = open("hw5-4_out.txt", "w", encoding = "utf-8")

for line in source:
    target.write(" ".join([dictEnRu[word] if word in dictEnRu.keys() else word for word in line.strip().split()])+"\n")

source.close()
target.close()

# Task 5

import random
random.seed(123)
numCount = random.randint(5, 10)
nums = [random.randrange(10000) for i in range(numCount)]

# Простой вариант: подсчитать сумму сразу
print(f"Сумма записанных чисел: {sum(nums)}")

with open("hw5-5_out.txt", "w+") as target:
    target.write(" ".join(map(str, nums)))
    
# Сложный вариант: прочитать только что записанные числа и посчитать их сумму
    target.seek(0)
    numsRead = target.readline().strip().split()

print(f"Сумма записанных чисел, считанных из файла: {sum(map(int, numsRead))}")

# Task 6

def processSubject(subjLine):
    total = 0
    subject, scores = subjLine.strip().split(":")
    for score in scores.split():
        try:
            total += int(score.split("(")[0])
        except:
            pass
    return subject, total

with open("./hw5-6_in.txt", "r") as source:
    scoresDict = {processSubject(line)[0]: processSubject(line)[1] for line in source.readlines()}

print(scoresDict)

# Task 7

from functools import reduce
import json

def processCompany(companyLine):
    # функция, обрабатывающая одну строку оригинального файла
    
    linelist = companyLine.strip().split()
    losses, gains, compType, compName = int(linelist.pop()), int(linelist.pop()), linelist.pop(), " ".join(linelist)
    return compName, gains - losses

# собираем все строки в словарь {название фирмы: прибыль}
with open("./hw5-7_in.txt", "r") as source:
    fullCompanyDict = {processCompany(line)[0]: processCompany(line)[1] for line in source.readlines()}

# извлекаем прибыль у тех фирм, где она больше нуля 
aboveZeroProfit = [i[1] for i in fullCompanyDict.items() if i[1] > 0]

# подсчитываем среднюю прибыль
if len(aboveZeroProfit) > 0:
    avgProfit = reduce(lambda x, y: x + y, aboveZeroProfit) / len(aboveZeroProfit)
    finalList = [fullCompanyDict, {"Средняя прибыль:": round(avgProfit, 3)}]
else:
    finalList = [fullCompanyDict, {"Средняя прибыль:": 0}]
    print("Ни одна компания не показала положительную прибыль, средняя прибыль взята за 0.")
 
# записываем json
with open("./hw5-7_out.json", "w") as target:
    json.dump(finalList, target)

# Проверяем, что все записано корректно
with open("./hw5-7_out.json", "r") as target:
    print(json.load(target))