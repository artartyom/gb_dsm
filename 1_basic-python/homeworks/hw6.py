# Task 1

from time import sleep
from itertools import cycle

class TrafficLight:
    
    def __init__(self, greenTime):
        self.__color = "красный"
        self.greenTime = greenTime
    
    def running(self):
        if self.__color != "красный":
            raise ValueError("Нельзя начать не с красного света. Сбросьте светофор методом .reset()")
        else:
            for waitTime, сolor in cycle([(7, "желтый"), (2, "зеленый"), (self.greenTime, "красный")]):
                print("Сейчас горит {} свет; для прекращения работы остановите программу.".format(self.__color))
                sleep(waitTime)
                self.__color = сolor

    def reset(self):
        self.__color = "красный"        
    
# Task 2

class Road:
    
    def __init__(self, l, w):
        self._length, self._width = l, w
    
    def asphaltMassKg(self, sqmMass, thickness = 1):
        massKg = self._length * self._width * sqmMass * thickness
        print("Масса асфальта составляет {} кг ({} тонн).".format(massKg, massKg / 1000))
        return 
    
# Task 3

class Worker:
    
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {"wage": wage, "bonus": bonus}
        
class Position(Worker):
    
    def get_full_name(self):
        fullname = " ".join([str(self.surname), str(self.name)])
        print("Полное имя: {}".format(fullname))
        return fullname
        
    def get_total_income(self):
        fullincome = sum([b for a,b in self._income.items()])
        print("Полный доход: {}".format(fullincome))
        return fullincome

# проверки

pPetr = Position("Петр", "Петринский", "серьезный шеф", 100000, 2000000)
print("{}\n{}\n{}\n{}".format(pPetr.name, pPetr.surname, pPetr.position, pPetr._income))
pPetr.get_full_name()
pPetr.get_total_income()

# Task 4

class Car:
    
    speedLimit = False

    def __init__(self, speed, color, name, is_police):
        if not isinstance(is_police, bool):
            raise TypeError("is_police должно быть булевым значением.")
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police
        self.running = False
        self.currentSpeed = 0
    
    def startIt(self):
        if not self.running:
            print("Сначала заведите машину...")
            return False
        else:
            return True
        
    def go(self):
        if not self.running:
            self.currentSpeed = self.speed
            self.running = True
            print("Машина стартовала и едет со скоростью {} км/ч.".format(self.currentSpeed))
        else:
            print("Машина уже едет! Текущая скорость {} км/ч.".format(self.currentSpeed))
    
    def stop(self):
        if self.startIt():
            self.running = False
            self.currentSpeed = 0
            print("Машина остановилась.")
    
    def turn(self, direction):
        if self.startIt():
            if self.currentSpeed > 0:                
                right = ["направо", "вправо", "право", "right", "r", "п"]
                left = ["налево", "влево", "лево", "left", "l", "л"]
                if direction.lower() in right:
                    print("Машина поворачивает направо.")
                elif direction.lower() in left:
                    print("Машина поворачивает налево.")
                else:
                    print("Направление поворота не опознано.")
            else:
                print("Машина стоит на месте и не может повернуть. Ускорьтесь.")
    
    def speedUp(self, value = 10):
        if self.startIt():
            self.currentSpeed += value
            print("Машина ускоряется на {} км/ч!".format(value))
            
    def slowDown(self, value = 10):
        if self.startIt():
            if self.currentSpeed > 0: 
                print("Машина замедляется на {} км/ч!".format(min(value, self.currentSpeed)))
                self.currentSpeed = max(self.currentSpeed-value, 0)
            else:
                print("Машина уже стоит на месте со включенным двигателем.")
    def show_speed(self):
        if self.startIt():
            if self.currentSpeed > 0:
                print("Машина едет со скоростью {} км/ч.".format(self.currentSpeed))
            else: 
                print("Машина стоит на месте со включенным двигателем.")
                
class TownCar(Car):
    
    speedLimit = 60
    
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    
    def show_speed(self):
        if self.startIt():
            if self.currentSpeed > 0:
                print("Машина едет со скоростью {} км/ч.".format(self.currentSpeed))
                if self.currentSpeed > TownCar.speedLimit:
                    print("Это на {} км/ч больше предела в {} км/ч для городских машин.".format(self.currentSpeed-TownCar.speedLimit, TownCar.speedLimit))
            else: 
                print("Машина стоит на месте со включенным двигателем.")
                
class WorkCar(Car):
    
    speedLimit = 40
    
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    
    def show_speed(self):
        if self.startIt():
            if self.currentSpeed > 0:
                print("Машина едет со скоростью {} км/ч.".format(self.currentSpeed))
                if self.currentSpeed > WorkCar.speedLimit:
                    print("Это на {} км/ч больше предела в {} км/ч для рабочих и грузовых машин.".format(self.currentSpeed-WorkCar.speedLimit, WorkCar.speedLimit))
            else: 
                print("Машина стоит на месте со включенным двигателем.")

class SportCar(Car):
        
    def __init__(self, speed, color, name):
        super().__init__(speed, color, " ".join([name, "Sport"]), False)
    
    def go(self):
        if not self.running:
            self.currentSpeed = self.speed
            self.running = True
            print("Машина стартовала с громким ревом! Теперь она едет со скоростью {} км/ч.".format(self.currentSpeed))
        else:
            print("Машина уже едет! Текущая скорость {} км/ч.".format(self.currentSpeed))
    
    def show_speed(self):
        if self.startIt():
            if self.currentSpeed > 0:
                print("Машина едет со скоростью {} км/ч.".format(self.currentSpeed))
                if self.currentSpeed > 120:
                    print("Это очень быстро, но это спортивная машина.")
            else: 
                print("Машина стоит на месте со включенным двигателем.")
                
class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, " ".join([name, "Police"]), True)
    
    def go(self):
        if not self.running:
            self.currentSpeed = self.speed
            self.running = True
            print("Машина стартовала и включила сирену! Теперь она едет со скоростью {} км/ч. Пиу-виу.".format(self.currentSpeed))
        else:
            print("Машина уже едет! Текущая скорость {} км/ч.".format(self.currentSpeed))
            
a = TownCar(100, "green", "Mazda")
b = WorkCar(50, "yellow", "Kamaz")
c = SportCar(250, "red", "Ferrari")
d = PoliceCar(60, "black", "Lincoln")
 
a.go()
b.go()
c.go()
d.go()           

a.show_speed()
b.show_speed()
c.show_speed()
d.show_speed()

a.slowDown(a.currentSpeed - TownCar.speedLimit)
b.slowDown(b.currentSpeed - WorkCar.speedLimit)

a.show_speed()
b.show_speed()

c.turn("left")
c.slowDown(10000)
c.show_speed()
c.stop()

# Task 5

class Stationery:
    
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print("Запуск отрисовки.")
        
class Pen(Stationery):
    
    def draw(self):
        print("Рисуем ручкой {}.".format(self.title))
        
class Pencil(Stationery):
    
    def draw(self):
        print("Рисуем карандашом {}.".format(self.title))
        
class Handle(Stationery):
    
    def draw(self):
        print("Рисуем маркером {}.".format(self.title))
        
a = Pen("Erich Krause")
b = Pencil("Koh-i-Noor")
c = Handle("Stabilo")
d = Stationery("noname")

a.draw()
b.draw()
c.draw()
d.draw()