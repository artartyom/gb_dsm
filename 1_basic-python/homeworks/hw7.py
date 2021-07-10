# Task 1

class Matrix:
    
    def __init__(self, listOfLists):
        if isinstance(listOfLists, list) and all([isinstance(x, list) for x in listOfLists]):
            if all([len(x) == len(listOfLists[0]) for x in listOfLists]):
                if all([
                        all([isinstance(j, int) or isinstance(j, float) for j in i])
                        for i in listOfLists]):
                    self.matrix = listOfLists
                else:
                    raise TypeError("Inappropriate data: must be int or float.")
            else:
                raise ValueError("Inappropriate nested list structure: dimensions mismatch.")
        else:
            raise TypeError("Class Matrix requires a nested list.")
            
    def __str__(self):
        return "\n".join([" ".join([str(j) for j in i]) for i in self.matrix])
    
    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
                res = [[self.matrix[i][j]+other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]        
                return Matrix(res)
            else:
                raise ArithmeticError("Matrix dimensions mismatch.")
        else:
            raise TypeError("Second operand is not a Matrix.")

# Task 2

from abc import ABC, abstractmethod

class Clothing(ABC): # Абстрактный класс. Не создаем его экземпляры
    
    wardrobe = [] # "Шкаф", в котором хранятся все экземпляры дочерних классов
    
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("Please use an integer to specify size.")
        Clothing.wardrobe.append(self)        
        self.size = size
    
    @abstractmethod
    def fabricUsed(): # Расчет количества использованной ткани для всего шкафа
        return(sum([x.fabricUsed for x in Clothing.wardrobe]))

class Overcoat(Clothing):
    
    @property
    def fabricUsed(self): # Количество использованной ткани для одного элемента одежды
        return self.size / 6.5 + 0.5

class Suit(Clothing):
    
    @property
    def fabricUsed(self): # Количество использованной ткани для одного элемента одежды
        return self.size * 2 + 0.3
    
suitA = Suit(172)
suitB = Suit(171)
coatA = Overcoat(52)
print(suitA.fabricUsed)
print(suitB.fabricUsed)
print(coatA.fabricUsed) # странный результат, но формула соответствует ТЗ ;)

print("Overall fabric used: {}".format(Clothing.fabricUsed()))

# Task 3

class Cell:

    def __init__(self, n_comp):
        if not isinstance(n_comp, int):
            raise TypeError("Number of cellular compartments should be an int.")
        self.n_comp = n_comp
        print("The new Cell contains {} compartments.".format(self.n_comp))
    
    def __isCell(self, obj):
        if not isinstance(obj, Cell):
            raise TypeError("Not a Cell!")
        return True
    
    def __str__(self):
        return "This cell contains {} compartments.".format(self.n_comp)
    
    def __add__(self, other):
        self.__isCell(other)
        return Cell(self.n_comp + other.n_comp)
    
    def __sub__(self, other):
        self.__isCell(other)
        return Cell(self.n_comp - other.n_comp)
    
    def __mul__(self, other):
        self.__isCell(other)
        return Cell(self.n_comp * other.n_comp)
    
    def __truediv__(self, other): # в методичке
        self.__isCell(other)
        print("Warning: Floor division.")
        return Cell(self.n_comp // other.n_comp)

    def __floordiv__(self, other): # на сайте
        self.__isCell(other)
        return Cell(self.n_comp // other.n_comp)
    
    def make_order(self, n):
        finStr = "\n".join(["*" * n for i in range(self.n_comp // n)])
        if self.n_comp % n != 0:
            if len(finStr) > 0:
                finStr += "\n"
            finStr += "*" * (self.n_comp % n)
        return finStr

a = Cell(10)
b = Cell(5)

try:
    a + 5
except TypeError:
    print("That did not work.")
    
c = a / b
print(c)

print(a.make_order(3))
print(a.make_order(5))
print(b.make_order(6))