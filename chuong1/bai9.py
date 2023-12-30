class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh

    def tinh_chu_vi(self):
        return self.so_canh * 3.14

    def tinh_dien_tich(self):
        pass


class HinhBinhHang(DaGiac):
    def __init__(self, so_canh, canh_dai, canh_be):
        super().__init__(so_canh)
        self.canh_dai = canh_dai
        self.canh_be = canh_be

    def tinh_chu_vi(self):
        return 2 * (self.canh_dai + self.canh_be)

    def tinh_dien_tich(self):
        return self.canh_dai * self.canh_be


class HinhChuNhat(HinhBinhHang):
    def __init__(self, canh_dai, canh_be):
        super().__init__(4, canh_dai, canh_be)


class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

hinh_binh_hang = HinhBinhHang(5, 3, 4)
print("Chu vi hình bình hành:", hinh_binh_hang.tinh_chu_vi())
print("Diện tích hình bình hành:", hinh_binh_hang.tinh_dien_tich())

hinh_chu_nhat = HinhChuNhat(6, 8)
print("Chu vi hình chữ nhật:", hinh_chu_nhat.tinh_chu_vi())
print("Diện tích hình chữ nhật:", hinh_chu_nhat.tinh_dien_tich())

hinh_vuong = HinhVuong(10)
print("Chu vi hình vuông:", hinh_vuong.tinh_chu_vi())
print("Diện tích hình vuông:", hinh_vuong.tinh_dien_tich())
