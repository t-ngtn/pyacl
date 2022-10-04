class V:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, a: "V") -> "V":
        return V(self.x + a.x, self.y + a.y)

    def __sub__(self, a: "V") -> "V":
        return V(self.x - a.x, self.y - a.y)

    def __mul__(self, a: "V"):  # dot
        return self.x * a.x + self.y * a.y

    def cross(self, a: "V"):  # self -> a
        return self.x * a.y - self.y * a.x

    def ccw(self, a: "V"):
        area = self.cross(a)
        if area > 0:
            return 1  # ccw
        elif area < 0:
            return -1  # cw
        else:
            return 0  # collinear
