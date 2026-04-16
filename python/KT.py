#Nhập danh sách số nguyên
lst = list(map(int, input("Nhập các số nguyên (cách nhau bởi dấu cách): ").split()))

#Chuyển thành tuple _t1
_t1 = tuple(lst)
print("_t1 ban đầu:", _t1)


'''
#loại bỏ số lẻ
_t1 = tuple(x for x in _t1 if x % 2 == 0)
print("Loại bỏ số lẻ:" ,_t1)
'''


#tách l1 dương l2 âm
L1 = [x for x in _t1 if x >= 0]
L2 = [x for x in _t1 if x <= 0]
print("L1", L1)
print("L2", L2)


#sắp xếp
L1.sort() #tăng dần
L2.sort(reverse=True) #giảm dần

print("L1 tăng", L1)
print("L2 giảm", L2)

#thêm 0
L1.insert(0,0) #thêm đầu
L2.append(0) #thêm cuối

print("L1", L1)
print("L2", L2)

#nối
_t2 = tuple (L2 + L1)
print(_t2)