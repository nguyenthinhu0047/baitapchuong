import math
class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinh_chu_vi(self):
        return self.a + self.b + self.c

    def tinh_dien_tich(self):
        # S = √(p(p - a)(p - b)(p - c))
        p = (self.a + self.b + self.c) / 2
        return round(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)


class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, math.sqrt(a ** 2 - b ** 2))


class TamGiacCan(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

        if a == b or b == c or c == a:
            self.can = True
        else:
            self.can = False


class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a, a)

        self.deu = True



tam_giac = TamGiac(3, 4, 5)
print("Chu vi tam giác:", tam_giac.tinh_chu_vi())
print("Diện tích tam giác:", tam_giac.tinh_dien_tich())

tam_giac_vuong = TamGiacVuong(3, 4)
print("Chu vi tam giác vuông:", tam_giac_vuong.tinh_chu_vi())
print("Diện tích tam giác vuông:", tam_giac_vuong.tinh_dien_tich())

tam_giac_can = TamGiacCan(3, 4, 4)
print("Chu vi tam giác cân:", tam_giac_can.tinh_chu_vi())
print("Diện tích tam giác cân:", tam_giac_can.tinh_dien_tich())

tam_giac_deu = TamGiacDeu(5)
print("Chu vi tam giác đều:", tam_giac_deu.tinh_chu_vi())
print("Diện tích tam giác đều:", tam_giac_deu.tinh_dien_tich())
