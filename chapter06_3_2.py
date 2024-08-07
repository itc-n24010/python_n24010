class Rectangle:
    angle = 90

    def __init__(self, width, height):
        self.name = 'Rectangle'
        self.width = width
        self.height = height
        self.perimeter = self.a_perimeter()
        self.area = self.a_area()

    def a_perimeter(self):
        w = self.width
        h = self.height
        return (w * 2) + (h * 2)

    def a_area(self):
        w = self.width
        h = self.height
        return w * h

    def result(self):
        x = self.angle
        n = self.name
        w = self.width
        h = self.height
        p = self.perimeter
        a = self.area
        print("名前: {}, 角度: {}, 幅: {}, 高さ: {}".format(n, x, w, h))
        print("周の長さ: {}, 面積: {}".format(p, a))

z1 = Rectangle(4, 3)
z1.result()


class square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)
        self.name = 'square'

l1 = square(5)
l1.result()
