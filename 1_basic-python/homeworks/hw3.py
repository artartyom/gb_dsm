# Task 1
def divider():
    
    # Запрашивает два числа и делит первое на второе
    
    a, b = float(input("Делимое: ")), float(input("Делитель: "))
    while b == 0:
        b = float(input("Пожалуйста, введите ненулевой делитель: "))
    return a / b

# Task 2

def addressbook(name, surname, birthYr, town, email, phone):

    # Формирует строку с записью для адресной книги из именованных аргументов
    
    print(f"Фамилия: {surname}\nИмя: {name}\nГод рождения: {birthYr}\nГород проживания: {town}\nТелефон: {phone}\nemail: {email}")
    
# Task 3

def my_func(a, b, c):
    
    # Возвращает сумму двух наибольших аргументов из трех полученных
    
    return sum(sorted([a, b, c])[1:])

my_func_lam = lambda a, b, c: sum(sorted([a, b, c])[1:]) # так быстрее

# Task 4

def toNegativePower(base, exponent):
    
    # Возведение в отрицательную степень без использования ** или pow()
    
    result, currentPower = base, 1
    while currentPower < abs(exponent):
        currentPower += 1
        result *= base
    return 1 / result


# Task 5

def sumInput():
    
    """
    До тех пор, пока не будет введено заданное стоп-слово, программа суммирует введенные через пробел числа
    Если стоп-слово введено внутри последовательности с числами, то эти числа будут также прибавлены
    При этом числа, введенные после стоп-слова, будут проигнорированы
    """
    
    result = 0
    stopword = input("Введите стоп-слово: ").lower()
    
    inputlist = input("Введите последовательность чисел. ").lower().split()
    
    while not stopword in inputlist:
        result += sum(map(int, inputlist))
        inputlist = input("Введите последовательность чисел. ").split()
    
    result += sum(map(int, inputlist[:inputlist.index(stopword)])) # сложить все числа до стоп-слова
    
    return result

# Task 6

int_func = lambda word: word.title() # превращает первую букву в заглавную

# Task 7

def capitalizer(inString):
    
    # делает заглавной первую букву каждого слова в строке из введенных через пробел слов
    
    print(" ".join(int_func(word) for word in inString.split()))


