class HocVien:
    def __init__(self,ht,email,dt,dc,lop):
        self.hoten=ht
        self.email=email
        self.dt=dt
        self.dc=dc
        self.lop=lop
    def showInfo(self):
        print("Họ tên: ",self.hoten)
        print("Email: ",self.email)
        print("Địa chỉ: ", self.dc)
        print("Điện thoại: ", self.dt)
        print("Lớp: ", self.lop)
    def setInfo(self,dc="Hà Nội",lop="14C22"):
        self.diachi=dc
        self.lop=lop


class Main:
    hv1=HocVien("Trần Mạnh Quân"," q@gmail.com","00","HN","14c2")
    hv1.showInfo
    print("_______-")