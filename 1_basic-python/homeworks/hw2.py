# Task 1

l1 = [1, 2.0, "tri", [4, 5.0, "shest"], (7, 8.0, "devyat"), {10: "11"}, bool(12)]

for element in l1:
    print("{} : type {}" .format(element, type(element)))

# Task 2

l2 = input("Введите элементы списка через пробел: ").split()

print("Было:\n{}" .format(l2))

# If len(l2) < 2: nothing happens
# If len(l2) % 2 == 1: last element will remain unchanged
for i in range(len(l2) // 2):
    l2[2*i], l2[2*i + 1] = l2[2*i + 1], l2[2*i]

print("Стало:\n{}" .format(l2))

# Task 3

# 3.1 - list
seasons = ["Зима", "Весна", "Лето", "Осень", "Зима"]
seasonNum = int(input("Введите номер месяца: "))
if seasonNum > 12 or seasonNum < 1:
    print("Такого месяца не существует")
else:
    print(seasons[seasonNum // 3])

# 3.2 - dict
seasons = {0 : "Зима",
           1 : "Весна",
           2 : "Лето",
           3 : "Осень",
           4 : "Зима"}
seasonNum = int(input("Введите номер месяца: "))
if seasonNum > 12 or seasonNum < 1:
    print("Такого месяца не существует")
else:
    print(seasons[seasonNum // 3])
    
# Task 4

inputWords = input("Введите несколько слов, разделенных пробелами: ").split()

for index, word in enumerate(inputWords):
    print("{}. {}" .format(index + 1, word[:10] if len(word) > 10 else word))
    
# Task 5

rating = input("Введите изначальный рейтинг: числа, разделенные пробелами.\n").split()
rating = [int(i) for i in rating]
rating.sort(reverse=True)

new_num = int(input("Введите значение рейтинга: "))
for i in range(len(rating)):

    if rating[i] < new_num:
        rating.insert(i, new_num)
        break
    
if i == len(rating) - 1: 
    # Эта конструкция работает только когда мы ничего не вставили в список
    # Если мы добавили число ранее, длина списка увеличивается, условие невыполнимо
    rating.append(new_num)

print(rating)

# Task 6

index = 1
inventory = []

while True: # loop to initialize the inventory
    
    name = input('Введите название товара.\nДля выхода введите "стоп".\n')
    if name.title() == "Стоп": 
        break
    
    cost = input('Введите цену товара.\nДля выхода введите "стоп".\n')
    if cost.title() == "Стоп":
        break
    else:
        cost = int(cost)
    
    quantity = input('Введите число единиц товара.\nДля выхода введите "стоп".\n')
    if quantity.title() == "Стоп":
        break
    else:
        quantity = int(quantity)
        
    units = input('Введите единицы измерения числа товаров.\nДля выхода введите "стоп".\n')
    if units.title() == "Стоп":
        break
    
    inventory.append((index, {"название" : name.lower(),
                                  "цена" : cost,
                                  "количество" : quantity,
                                  "ед" : units.lower()})) # create an entry
    index += 1 #increment index
    
analyticsDict = {"название" : [inventory[i][1]["название"] for i in range(len(inventory))],
                 "цена" : [inventory[i][1]["цена"] for i in range(len(inventory))],
                 "количество" : [inventory[i][1]["количество"] for i in range(len(inventory))],
                 "ед" : [inventory[i][1]["ед"] for i in range(len(inventory))]}

# Здесь не происходит отбора только уникальных значений для единиц измерения, тк это показалось мне более практически применимым
# Если принципиально важно отобрать только уникальные значения, можно поместить генератор в list(set())

print(analyticsDict)