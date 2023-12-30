class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phoi(self):
        tu_so = int(input("Nhập tử số: "))
        mau_so = int(input("Nhập mẫu số: "))
        self.tu_so = tu_so
        self.mau_so = mau_so

    def in_phoi(self):
        print(f"{self.tu_so}/{self.mau_so}")

# Sử dụng lớp PhanSo5
ps = PhanSo(3, 4)
print(ps.kiem_tra_hop_le())

ps.nhap_phoi()
ps.in_phoi()
