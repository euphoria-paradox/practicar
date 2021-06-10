class Rectangle():
    rects= []
    def __init__(self, width , length):
        self.width = width
        self.length = length
        self.rects.append((self.width, self.length))


rect1 = Rectangle(5 ,16)
rect2 = Rectangle(6 , 18)
rect3 = Rectangle(2 ,10)

print(Rectangle.rects)
