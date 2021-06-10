class Square():
    square_list = []
    
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)


sq1 = Square(10)
sq2 = Square(12)
sq3 = Square(4)

print(Square.square_list)


'''
def funcs(obj1 ,obj2):
    return obj1 is obj2

class Square:
    def __init__(self):
        pass

s = Square()

t = Square()

print(funcs(s,t))
'''
