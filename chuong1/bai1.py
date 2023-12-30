
class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def in_thong_tin(self):
        print("Chiều dài: ", self.chieu_dai)
        print("Chiều rộng: ", self.chieu_rong)
        print("Chu vi: ", self.tinh_chu_vi())
        print("Diện tích: ", self.tinh_dien_tich())


hcn = HinhChuNhat(0, 0)
hcn.nhap_du_lieu()
hcn.in_thong_tin()
