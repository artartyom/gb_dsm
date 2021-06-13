# Task 1

a = 123
b = 123.0
c = "123"
d = True

usr_str, usr_int, usr_float = input("please enter text: "), int(input("please enter a number: ")), int(input("please enter a number: "))*1.0

print("{} is an int, {} is a float, '{}' is a string, {} is a boolean" .format(a, b, c, d))
print("'{}' is a string, {} is an int, {} is a float" .format(usr_str, usr_int, usr_float))

# Task 2

time = int(input("Введите число секунд: "))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 3600 % 60

print("{}:{}:{}" .format(hours, minutes, seconds))

# Task 3

# nn = 11*n; nnn = 111*n; therefore, n+nn+nnn = 123n
print(123 * int(input("Введите число: ")))

# Task 4

worknum = int(input("Введите целое положительное число: "))
maxnum = 0

while worknum > 0:
    if worknum % 10 > maxnum:
        maxnum = worknum % 10
    worknum = worknum // 10

print(maxnum)

# Task 5

revenue = float(input("Введите выручку: "))
expenses = float(input("Введите расходы: "))

if revenue > expenses:
    income = revenue - expenses
    print("Фирма приносит прибыль.")
    print("Рентабельность выручки: {}%" .format(100 * income / revenue))
    print("Прибыль на одного сотрудника: {}" .format(income / int(input("Введите число сотрудников:"))))
elif revenue < expenses:
    print("Фирма приносит убытки.")
else:
    print("Убытки равны доходам!")
    
# Task 6

a, b = int(input("Сколько километров в первый день? ")), int(input("Целевая дистанция? "))
day = 1

while a < b:
    day += 1
    a *= 1.1
print(day)