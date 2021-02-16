"""
 y^2 = x^3 +ax + b
 должно быть: 4a^3 + 27b^2 != 0
 0 - бесконечно удалённая точка
 j = 1728 * (4a^3/(4a^3 + 27b^2))
 Дискриминант: -16(4a^3 + 27b^2)
 P + Q = R
 P + 0 = 0 + P = P

"""


class EllipticCurve:
    a = int(0)
    b = int(0)
    p = int(0)

    def set(self, aIn: int, bIn: int, pIn: int):
        self.a = aIn
        self.b = bIn
        self.p = pIn


class Point:
    x = float(0)
    y = float(0)
    curve = EllipticCurve()

    def set(self, xIn: int, yIn: int, cIn: EllipticCurve):
        self.x = xIn
        self.y = yIn
        self.curve = cIn

    def print(self):
        print(self.x, self.y)

    def __add__(self, other):
        result = Point()
        if self.curve != other.curve:
            return ArithmeticError
        if (self.x == other.x) and (self.y == other.y):
            alpha = (3 * self.x * self.x + self.curve.a) / (2 * self.y)
        else:
            alpha = (other.y - self.y) / (other.x - self.x)
        result.x = alpha * alpha - self.x - other.x
        result.y = -self.y + alpha * (self.x - result.x)
        return result

    def __iadd__(self, other):
        result = Point()
        if self.curve != other.curve:
            return ArithmeticError
        if (self.x == other.x) and (self.y == other.y):
            alpha = (3 * self.x * self.x + self.curve.a) / (2 * self.y)
        else:
            alpha = (other.y - self.y) / (other.x - self.x)
        result.x = alpha * alpha - self.x - other.x
        result.y = -self.y + alpha * (self.x - result.x)
        self.x = result.x
        self.t = result.y


    # def __mul__(self, other):
    #     if type
    #     result = Point()
    #     if self.curve != other.curve:
    #         return ArithmeticError
    #     if (self.x == other.x) and (self.y == other.y):
    #         alpha = (3 * self.x * self.x + self.curve.a) / (2 * self.y)
    #     else:
    #         alpha = (other.y - self.y) / (other.x - self.x)
    #     result.x = alpha * alpha - self.x - other.x
    #     result.y = -self.y + alpha * (self.x - result.x)
    #     return result


class ECP:
    q = int(0)

    P = Point()
    Q = Point()

    curve = EllipticCurve()

    def __init__(self, PIn: Point, QIn: Point, cIn: EllipticCurve, qIn: int):
        self.P = PIn
        self.P.print()
        self.q = qIn
        self.curve = cIn
        self.Q = QIn


    def signature(self, d: int):
        r = int(0)
        C = Point()
        C.set(0, 0, self.curve)
        s = int(0)

        #alpha = hash(msg)
        e = 0x2DFBC1B372D89A1188C09C52E0EEC61FCE52032AB1022E8E67ECE6672B043EE5#e = alpha % q
        if (e == 0):
            e = 1

        k = 0x77105C9B20BCD3122823C8CF6FCC7B956DE33814E95B7FE64FED924594DCEAB3  # random.uniform(0, q)

        while (s == 0):
            while (r == 0):
                C.set(0, 0, self.curve)
                for i in range(k):
                    C = C + self.P
                r = C.x % self.q
            C.print()
            s = (r * d + k * e) % self.q
        return str(r) + str(s)


if __name__ == '__main__':

    # Заполнение параметров Эллитической кривой, Точек, q,
    curve = EllipticCurve()
    curve.set(7, 0x5FBFF498AA938CE739B8E022FBAFEF40563F6E6A3472FC2A514C0CE9DAE23B7E,
              0x8000000000000000000000000000000000000000000000000000000000000431)
    m = 0x8000000000000000000000000000000150FE8A1892976154C59CFC193ACCF5B3
    q = 0x8000000000000000000000000000000150FE8A1892976154C59CFC193ACCF5B3

    P = Point()
    P.set(2, 0x8E2A8A0E65147D4BD6316030E16D19C85C97F0A9CA267122B96ABBCEA7E8FC8, curve)

    keySig = 0x7A929ADE789BB9BE10ED359DD39A72C11B60961F49397EEE1D19CE9891EC3B28

    Q = Point()
    Q.set(0x7F2B49E270DB6D90D8595BEC458B50C58585BA1D4E9B788F6689DBD8E56FD80B,
          0x26F1B489D6701DD185C8413A977B3CBBAF64D1C593D26627DFFB101A87FF77DA, curve)
    C = Q + P
    C.print()
    e = 0x2DFBC1B372D89A1188C09C52E0EEC61FCE52032AB1022E8E67ECE6672B043EE5
    k = 0x77105C9B20BCD3122823C8CF6FCC7B956DE33814E95B7FE64FED924594DCEAB3
    d = int(0x7A929ADE789BB9BE10ED359DD39A72C11B60961F49397EEE1D19CE9891EC3B28)
    test = ECP(P, Q, curve, q)

    test.signature(d)


    #test.signature(d)

"""
    test = int(input("enter value: "))
    test += 5
    if test == 15:
        print("число = 15")
    if type(test) == int:
        print("input - int")

    print(test)

    d1 = []
    d1 = [1, 2, 3, 4, 5, 6]
    d2 = [8, 9, 10]
    d1.append(7)
    d1.extend(d2)
    big = 123123123123123123321312323123123123

    print(big)
    for j in range(5):
        d2 = []
        for i in range(5):
            d2.append(0)
        d1.append(d2)
"""
