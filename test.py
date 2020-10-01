def dupl(a):
    a.sort()
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            return 1
    return 0

class Rectangle:
    def __init__(self, list_of_dots = []):
        list_of_dots.sort()
        list_of_dots.sort(key=lambda elem: elem[1])
        self.dots = list_of_dots
        
        if self.dots[0][1] != self.dots[1][1]:            
            self.not_rectangle = 1
            return
        if self.dots[0][0] != self.dots[2][0]:
            self.not_rectangle = 1
            return
        if self.dots[3][0] != self.dots[1][0] or self.dots[3][1] != self.dots[2][1]:
            self.not_rectangle = 1
            return
        
        self.not_rectangle = 0
        self.a = self.dots[1][0] - self.dots[0][0]
        self.b = self.dots[2][1] - self.dots[0][1]

    def perimetr(self):
        if self.not_rectangle:
            return "not_rectangle"
        return 2*(self.a+self.b)
    
    def square(self):
        if self.not_rectangle:
            return "not_rectangle"
        return self.a*self.b

a = Rectangle([[5,0],[0,5],[0,0],[5,5]])
b = Rectangle([[7,0],[0,5],[0,0],[5,5]])

print(a.perimetr())
print(a.square())
print(b.perimetr())
print(b.square())
