'''
n = int(input("Nhập n: "))
for i in range(n):
    print (f'2*{i}={2*i}')
'''

'''
n = int(input("Nhập n: "))
if n > 10:
    print ("Số phải < 10")
else:
    for i in range(2,n,2):
        print(i)
'''

'''
for i in range(80,101):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
'''

'''
n = int(input("Nhập n: "))
if n >= 20:
    print("Nhập n < 20")
else:
    for i in range(n+1):
        if i % 5 == 0 or i % 7 == 0:
            print(i)
'''

'''

count = 0
n = 0
while (count < 9):
    print ('Số thứ', n, 'là: ', count)
    n = n+1
    count = count + 1
print("Finisth")
'''
'''
tich = 1
for i in range(1,11):
    tich *=i
    print(tich)
'''

'''
n = int(input("Nhập số nguyên dương n: "))
if n < 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *=i
    print(f'{n}! =', giai_thua)
'''
'''

n = int(input("Nhập số nguyên dương n: "))
if n < 2:
    print("Không phải số nguyên tố!")
else:
    la_snt = True
    for i in range(2, int(n**0.5) +1):
        if n % 1 == 0:
            la_snt = False
            break
    if la_snt:
        print("Đây là số nguyên tố")
    else: 
        print("Đây không phải số nguyên tố")
        '''

'''
def sayhello(name):
    return "Hello " + name
text = sayhello("Tran Manh Quan")
print(text)
'''
'''
def tonghieu(x,y):
    tong = x + y
    hieu = x - y
    return tong, hieu
t,h =tonghieu(2,8)
print('tổng là: ', t)
print('hiệu là: ', h)
'''
'''
def tong(a,b):
    return a + b
kq = tong(5,6)
print(kq)
'''
'''
def tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong
print(tong(1, 2, 3, 4, 5))
'''
'''
def songuyento(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập n: "))
if songuyento(n):
    print("Đây là số nguyên tố")
else:
    print("Đây không phải số nguyên tố")
'''

'''
def songuyento(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5), + 1):
        if n % i == 0:
            return False
    return True
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print(f'Các số nguyên tố trong khoảng [{a}, {b}]')
'''