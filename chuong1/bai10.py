class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Elip(Diem):
    def __init__(self, a, b, h, k):
        super().__init__(h, k)
        self.a = a
        self.b = b

    def tinh_dien_tich(self):
        return 3.14 * self.a * self.b


class DuongTron(Elip):
    def __init__(self, r, h, k):
        super().__init__(r, r, h, k)


# Ví dụ sử dụng
elip = Elip(5, 3, 0, 0)
print("Diện tích elip:", elip.tinh_dien_tich())

duong_tron = DuongTron(3, 0, 0)
print("Diện tích đường tròn:", duong_tron.tinh_dien_tich())