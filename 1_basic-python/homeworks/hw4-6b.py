# task 6-b

from itertools import cycle

for food in cycle(["сосиски", "бутерброд", "яичницу", "фрукты", "кашу"]):
    print("Едим {}!".format(food))
    
    doWeBreak = input('Продолжаем завтракать? Всегда можно сказать "нет" ').lower()
    
    if doWeBreak == "нет":
        break

print("Голодаем...")