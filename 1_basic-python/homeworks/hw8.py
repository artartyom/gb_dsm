# Task 1

class Date:
    
    day, month, year = 0, 0, 0
    dateDict = {1: 31,
                2: 28,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31}
    
    @classmethod
    def set(cls, dateString):
        try:
            if len(dateString.split("-")) != 3:
                raise SyntaxError()
            else:
                cls.day, cls.month, cls.year = [int(x) for x in dateString.split("-")]
        except ValueError:
            print("Некорректные данные - используйте числа.")
        except SyntaxError:
            print('Строка не соответствует формату "день-месяц-год".')
                
    @staticmethod
    def validate():
        if not Date.month in Date.dateDict.keys():
            print("Некорректный месяц. Введите месяц от 1 до 12.")
        elif Date.day < 1 or Date.day > Date.dateDict[Date.month]:
            print("Некорректное число дней для указанного месяца.")
        elif Date.year < 1 or Date.year > 9999:
            print("Некорректно введен год. Введите год от 1 до 9999.")
        else:
            print("Введенная дата корректна.")
    
# Task 2

class ZeroDiv(Exception):
    
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        print("Для выхода введите любой текст.")
        a, b = float(input("Введите делимое: ")), float(input("Введите делитель: "))
        if b == 0:
            raise ZeroDiv("Делить на ноль нельзя!")
        else:
            print("Результат деления: {}".format(a/b))
    except ZeroDiv as err:
        print(err)
    except ValueError:
        print("Покидаю программу.")
        break
    
# Task 3

class NotNumber(Exception):
    
    def __init__(self):
        print("Введенное значение не является числом. Введите число")
        super().__init__
        
print("Для выхода введите stop.")
resList = []

while True:
    
    try:
        a = input("Введите число или команду stop для выхода: ")
        if not a.isdecimal():
            if not a.lower() == "stop":
                raise NotNumber()
            else:
                break
        else:
            resList.append(int(a))
            
    except NotNumber:
        pass

print("Итоговый список: {}.".format(resList))

# Tasks 4, 5, 6

from abc import ABC, abstractmethod

class Warehouse:
    
    def __init__(self, max_items):
        self.appliances = {}
        self.max_items = max_items
        self.storedItems = 0
        
    def __checkCapacity(self, addCount):
        if self.max_items - self.storedItems == 0:
            print("Error. Warehouse is at full capacity!")
            return 0
        elif self.max_items - self.storedItems < addCount:
            print("Warning. Warehouse can't hold that many items. Adding up to full capacity.")
            return self.max_items - self.storedItems
        else:
            print("Adding items.")
            return addCount
    
    def __checkSubtraction(self, applianceType, removeCount):
        if not applianceType in self.appliances.keys():
            raise TypeError("Appliance not found!")
        if self.appliances[applianceType][0] < removeCount:
            print("Warning. Too little appliances of that time. Removing all remaining appliances of that type.")
            return self.appliances[applianceType][0]
        else:
            print("Removing items.")
            return removeCount
        
    def __str__(self):
        outstr = "Max capacity: {} items.\nCurrently stored: {} items.\n".format(self.max_items, self.storedItems)
        outstr += "\n".join([("{}: {} items.".format(i, len(self.appliances[i][1]))) for i in self.appliances.keys()])
        return outstr
        
    def addAppliance(self, appliance, count): # Метод, отвечающий за прием техники на склад
        if not isinstance(appliance, Appliance):
            raise TypeError("Can only add appliances.")
        if not isinstance(count, int):
            raise TypeError("Use an integer for appliance count")
        realCount = self.__checkCapacity(count)
        if realCount > 0:
            if not str(appliance).split("\n")[0] in self.appliances.keys():
                self.appliances[str(appliance).split("\n")[0]] = [realCount, [appliance for x in range(realCount)]]
                self.storedItems += realCount
            else:
                self.appliances[str(appliance).split("\n")[0]][0] += realCount
                self.appliances[str(appliance).split("\n")[0]][1].extend([appliance for x in range(realCount)])
                self.storedItems += realCount
    
    def removeAppliance(self, applianceType, count): # Метод, отвечающий за передачу техники со склада
        if not isinstance(applianceType, str):
            raise TypeError("Use a string to denote appliance type.")
        if not isinstance(count, int):
            raise TypeError("Use an integer for appliance count")
        realCount = self.__checkSubtraction(applianceType, count)
        poppedItems = self.appliances[applianceType][1][:realCount]
        self.storedItems -= realCount
        if len(self.appliances[applianceType][1]) > realCount:
            self.appliances[applianceType][0] -= realCount
            self.appliances[applianceType][1] = self.appliances[applianceType][1][realCount:]
        else:
            del self.appliances[applianceType]
        return poppedItems
    
class Appliance(ABC): # Абстрактный класс - мы не собираемся создавать безымянную технику

    @abstractmethod
    def __init__(self, name, make, paper_format):
        self.name = name
        self.paper_format = paper_format
        self.make = make

    def addToWarehouse(self, warehouse, count):
        if not isinstance(warehouse, Warehouse):
            raise TypeError("Can only add to a Warehouse!")
        else:
            warehouse.addAppliance(self, count)
    
class Printer(Appliance):
    def __init__(self, name, make, paper_format, is_bw, printSpeed, twoSidedPrint):
        self.is_bw = is_bw
        self.printSpeed = printSpeed
        self.twoSidedPrint = twoSidedPrint
        super().__init__(name, make, paper_format)
        print("Создан новый объект: принтер {}.".format(" ".join([self.make, self.name])))
    
    def __str__(self):
        return "Printer\nModel: {}\nMake: {}\nPaper format: {}\nBlack and white only: {}\nPrints on two sides: {}\nPrint speed: {} sheets per minute".format(self.name, self.make, self.paper_format, self.is_bw, self.twoSidedPrint, self.printSpeed)
    
class Scanner(Appliance):
    def __init__(self, name, make, paper_format, outputFormats, scanSpeed):
        self.outputFormats = outputFormats
        self.scanSpeed = scanSpeed
        super().__init__(name, make, paper_format)
        print("Создан новый объект: сканер {}.".format(" ".join([self.make, self.name])))
            
    def __str__(self):
        return "Scanner\nModel: {}\nMake: {}\nPaper format: {}\nOutput formats: {}\nScan speed: {} sheets per minute".format(self.name, self.make, self.paper_format, ", ".join(self.outputFormats), self.scanSpeed)

class Xerox(Appliance):
    def __init__(self, name, make, paper_format, canJustScan, canJustPrint, isBW, twoSidedPrint, speed):
        self.canJustScan = canJustScan
        self.canJustPrint = canJustPrint
        self.isBW = isBW
        self.twoSidedPrint = twoSidedPrint
        self.speed = speed
        super().__init__(name, make, paper_format)
        print("Создан новый объект: ксерокс {}.".format(" ".join([self.make, self.name])))
        
    def __str__(self):
        return("Xerox\nModel: {}\nMake: {}\nPaper format: {}\nBlack and white only: {}\nSpeed: {} sheets per minute\nCan work as a scanner: {}\nCan work as a printer: {}".format(self.name, self.make, self.paper_format, self.isBW, self.speed, self.canJustScan, self.canJustPrint))
    
wh1 = Warehouse(10)

printer1 = Printer("A1000", "Epson", "A4", False, 10, True)
print(printer1)
printer1.addToWarehouse(wh1, 4)

scanner1 = Scanner("S10-A2", "Epson", "A2", ["pdf", "jpg", "png"], 4)
print(scanner1)
scanner1.addToWarehouse(wh1, 2)

xerox1 = Xerox("Ultima", "Xerox", "A3", True, True, False, True, 35)
print(xerox1)
xerox1.addToWarehouse(wh1, 8)

print(wh1)
removedXeroxes = wh1.removeAppliance("Xerox", 3)
print(removedXeroxes)
wh1.addAppliance(Xerox("Business Eco Plus", "Xerox", "A4", False, False, True, True, 20), 4)
print(wh1)

# Task 7

class ComplexNumber:
    
    def __init__(self, realPart, imagPart):
        try:
            self.realPart = int(realPart) if float(realPart) % 1 == 0 else float(realPart)
            self.imagPart = int(imagPart) if float(imagPart) % 1 == 0 else float(imagPart)
        except ValueError:
            print("Please use integers or floats for the real and the imaginary parts.")
            
    def __str__(self):
        if self.realPart != 0:
            if self.imagPart > 0:
                return "{}+{}i".format(self.realPart, self.imagPart)
            elif self.imagPart == 0:
                return str(self.realPart)
            else:
                return "{}{}i".format(self.realPart, self.imagPart)
        else:
            if self.imagPart != 0:
                return "{}i".format(self.imagPart)
            else:
                return str(self.realPart)

        
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            if self.imagPart - other.imagPart != 0:
                return ComplexNumber(self.realPart + other.realPart, self.imagPart + other.imagPart)
            else:
                return self.realPart - other.realPart        
        else:
            return ComplexNumber(self.realPart - other, self.imagPart)
    
    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            if self.imagPart + other.imagPart != 0:
                return ComplexNumber(self.realPart - other.realPart, self.imagPart - other.imagPart)
            else:
                return self.realPart - other.realPart
        else:
            return ComplexNumber(self.realPart - other, self.imagPart)
        
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber((self.realPart * other.realPart - self.imagPart * other.imagPart), (self.realPart * other.imagPart + self.imagPart * other.realPart))
        else:
            return ComplexNumber(self.realPart * other, self.imagPart * other)
        
    def __truediv__(self, other):
        if not isinstance(other, ComplexNumber):
            return ComplexNumber(self.realPart / other, self.imagPart / other)
        else:
            numerator = self * ComplexNumber(other.realPart, -1*other.imagPart)
            denominator = other.realPart**2 + other.imagPart**2
            return ComplexNumber(numerator.realPart / denominator, numerator.imagPart / denominator)
            
a = ComplexNumber(2, 2)
b = ComplexNumber(3, -1)
c = ComplexNumber(1, 3)

print(a + b) # (2+2i) + (3-1i) = 5+1i
print(a - b*2) # (2+2i) - 2*(3-1i) = (2+2i) - (6-2i) = -4
print(b * c) # (3-1i) * (1 + 3i) = (3-(-3)) + (9i-1i) = 6+8i
print(a / 2) # (2+2i) / 2 = 1+1i
print(a / (b*3)) # (2+2i) / (3*(3-1i)) = 0.13333 + 0.26667i
