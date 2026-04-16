'''
# Membership trong string
str1 = "javapoint"
str2 = 'sssit'
str4 = 'java'
str5 = "it"

_a = str4 in str1
print('str4 in str1', _a)

_b = str5 in str2
print('str5 in str2', _b)

_c = str4 not in str1
print('str4 not in str1',_c)
'''

'''
#Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
#Nhập chuỗi từ bàn phím
chuoi = input("Nhập chuỗi số cách nhau bằng dấu phẩy: ")
#tách chuỗi thành danh sách
danh_sach = chuoi.split(",")
#chuyển sang số nguyên tố
so_nguyen = [int(x) for x in danh_sach]
#lọc các số nguyên tố
so_nguyen_to = [x for x in so_nguyen if la_so_nguyen_to(x)]
#in
print("các số nguyên tố là: ", so_nguyen_to)
'''


#Nhập tên
ten = input("Nhập tên: ")

#loại bỏ khoảng trắng đầu cuối
ten = ten.strip()

#tách các từ theo khoảng trắng
danh_sach = ten.split()

#chuẩn hóa từ
ket_qua = []
for tu in danh_sach:
    tu = tu.lower() #chuyển hết về chữ thường
    tu = tu.capitalize() #chuyển chữ cái đầu thành chữ hoa 
    ket_qua.append(tu) #thêm vào danh sách

#ghép lại thành chuỗi hoàn chỉnh
ten_chuan = " ".join(ket_qua)

print("Họ tên chuẩn hóa:", ten_chuan)