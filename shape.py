class Shape():
        def __init__(self, shape):
            self.shape = shape
        def what_am_i(self):
            print("I am a " +self.shape)

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.shape = "Rectangle"
    def calculate_perimeter(self):
        return 2*(self.width+self.length)

class Square( Shape):
    def __init__(self , s1):
        self.s1= s1
        self.shape = 'Square'

    def calculate_perimeter(self):
        return 4*self.s1


rect = Rectangle(5 , 15)
print(rect.calculate_perimeter())
rect.what_am_i()

squ = Square(4)
print(squ.calculate_perimeter())
squ.what_am_i()
