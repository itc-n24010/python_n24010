class cylinder:
    pi = 3.14

    def __init__(self, radius=1, height=1):
        self.radius = float(radius)
        self.height = float(height)

    def base_area(self):
        '''底面積'''
        pi = cylinder.pi
        r = self.radius
        return pi * r ** 2

    def side_area(self):
        '''側面積'''
        pi = cylinder.pi
        r = self.radius
        h = self.height
        return 2 * r * pi * h

    def surface_area(self):
        '''表面積'''
        c = self.base_area()
        s = self.side_area()
        return 2 * c + s

    def volume(self):
        '''体積'''
        c = self.base_area()
        h = self.height
        return c * h

    def show_result(self):
        '''結果'''
        r = self.radius
        h = self.height
        S = self.surface_area()
        V = self.volume()

        print("半径: {}, 高さ: {}, 表面積: {}, 体積: {}".format(r, h, S, V))

c1 = cylinder()
c1.show_result()
c2 = cylinder(2., 4.)
c2.show_result()
c3 = cylinder(3., 5.)
c3.show_result()
c4 = cylinder(7., 1.)
c4.show_result()
