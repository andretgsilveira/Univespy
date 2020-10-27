class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def get(self):
        return self.x, self.y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __len__(self):
        return 2

    def __eq__(self, other):
        if type(other) == Point:
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        else:
            if self.x == other and self.y == other:
                return True
            else:
                return False


p = Point(1, 2)
q = Point(1, 2)
