n = int(input())
l =[]
for i in range(n):
    s = int(input())
    l.append(s)
#Nhập số X và đếm số lần X xuất hiện
x = int(input())
soLan = l.count(x)
print(f"Số lần số {x} xuất hiện trong list là: {soLan}")

#Thay thế phần tử từ vị trí 2 -> 7 trong list thành [8, 5, 4, 0, 1, 3].
l[2:8] = [8, 5, 4, 0, 1, 3]
print(f"Danh sách sau khi thay thế:",l)

#Tìm số lớn nhất, và nhỏ nhất trong list.
soLonNhat = max(l)
soNhoNhat = min(l)
print(f"Số lớn nhất là trong list là: {soLonNhat}")
print(f"Số nhỏ nhất là trong list là: {soNhoNhat}")

#Nhập một số Y tùy chọn từ bàn phím. Chèn số Y vào đầu list.
y = int(input())
l.insert(0, y)
print(f"Danh sách sau khi chèn y là:", l)

#Sau khi chèn số Y, kiểm tra các số trong list có sắp xếp theo thứ tự tăng dần hay giảm dần không. Nếu sắp xếp theo tăng dần thì in ra màn hình “TĂNG”, còn nếu sắp xếp theo thứ tự giảm dần thì in ra màn hình “GIÁM”, nếu không tăng không giảm thì in “NO”.
if l == sorted(l):
    print("TĂNG")
elif l == sorted(l, reverse=True):
    print("GIẢM")
else:
    print("NO")

#Tạo một list mới có N phần tử. Các phần tử sẽ có vị trí từ 1 -> N. Với mỗi phần tử ở vị trí i (1 <= i <= N) giá trị của nó là tổng i phần tử đầu tiên của list cũ.
lst_tong = []
sum = 0
for s in l:
    sum += s
    lst_tong.append(sum)
print(lst_tong)

#Tạo list mới
lst_new = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
lst_tang = sorted(lst_new)
lst_ttd = sorted(lst_new, key=abs)
print(lst_tang)
print(lst_ttd)

