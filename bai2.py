k = int(input())
a =[]
for i in range(k):
    s = int(input())
    a.append(s)

n = int(input("Nhập số dòng n:"))
m = int(input("Nhập số cột m: "))

if n * m > k:
    print("NO")
else:
    x = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        x.append(row)
    
    for row in x:
        print(row)