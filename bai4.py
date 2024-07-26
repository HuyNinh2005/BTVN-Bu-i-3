n = input("Nhập họ tên: ")
#Loại bỏ khoảng trắng ở đầu và cuối
ten = n.strip()

#Tách các từ
ten1 = ten.split()

# Viết hoa chữ cái đầu tiên của mỗi từ và viết thường các chữ cái còn lại
tuNew = [tu.capitalize() for tu in ten1]

#Ghép và các từ cách nhau một khoảng trắng
tuHoanChinh = " ".join(tuNew)
print(tuHoanChinh)