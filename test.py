def dupl(a):
    a.sort()
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            return 1
    return 0

class Rectangle:
    def __init__(self, list_of_dots = []):
        self.dots = list_of_dots
    def perimetr(self):
        return self.dots[1][1] - self.dots[0][1] + self.dots[2][0] - self.dots[1][0] + self.dots[2][1] - self.dots[3][1] + self.dots[3][0] - self.dots[0][0]
    def square(self):
        return (self.dots[1][1] - self.dots[0][1])*(self.dots[2][0] - self.dots[1][0])

a = Rectangle([[0,0],[0,5],[5,5],[5,0]])

print(a.perimetr())
print(a.square())
