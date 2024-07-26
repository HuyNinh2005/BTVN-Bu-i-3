s1 = input("Nhập chuỗi s1:")
s2 = input("Nhập chuỗi s2:")

s1_new = s1[::-1]
print(f"Đảo ngược của chuỗi s1 là: {s1_new}")

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

if 1 <= a < b <= len(s2):
    part_reversed_s2 = s2[:a-1] + s2[a-1:b][::-1] + s2[b:]
    print(f"Chuỗi s2 sau khi đảo ngược từ vị trí {a} đến {b}: {part_reversed_s2}")
else:
    print("NO")

# Tạo chuỗi s3 sau khi xóa các ký tự ở vị trí chẵn của s1
s3 = ''.join([s1[i] for i in range(len(s1)) if i % 2 != 0])
print(f"Chuỗi s1 sau khi xóa các ký tự ở vị trí chẵn: {s3}")

# Tạo chuỗi s4 đan xen các ký tự của s1 và s2
s4 = ''.join([i + j for i, j in zip(s1, s2)])
s4 += s1[len(s2):] + s2[len(s1):]  # Thêm phần còn lại của chuỗi dài hơn nếu có
print(f"Chuỗi đan xen s1 và s2: {s4}")

# Đổi chỗ 2 ký tự đầu tiên của 2 chuỗi và in ra kết quả
if len(s1) >= 2 and len(s2) >= 2:
    swapped_s1 = s2[:2] + s1[2:]
    swapped_s2 = s1[:2] + s2[2:]
    print(f"Chuỗi s1 sau khi đổi chỗ 2 ký tự đầu tiên: {swapped_s1}")
    print(f"Chuỗi s2 sau khi đổi chỗ 2 ký tự đầu tiên: {swapped_s2}")
else:
    print("NO")