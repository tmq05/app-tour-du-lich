class HocVien:
    def __init__(self,ht,email,dt,dc,lop):
        self.hoten=ht
        self.email=email
        self.dienthoai=dt
        self.diachi=dc
        self.lop=lop
    def showInfo(self):
        print("Họ tên: ", self.hoten)
        print("E-Mail: ", self.email)
        print("Điện thoại : ", self.dienthoai)
        print("Địa chỉ: ", self.diachi)
        print("Lớp: ", self.lop)
    def setInfo(self, dc="Hà Nội", lop="IT12.x"):
        self.diachi=dc
        self.lop=lop

class Main:
    hv1=HocVien("Quan","2@ss","00","HN","IT")
    hv1.showInfo()
    print("_______")
    hv1.setInfo()
    hv1.showInfo()
    print("_______")
    hv1.setInfo("Bắc Ning","ITITIT")
    hv1.showInfo()