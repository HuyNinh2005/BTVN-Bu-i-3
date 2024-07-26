n = int(input())
numbers = list(map(int, input().split()))
# Các số thầy Ba thích 
chu_so_thich = {'1', '3', '5', '7', '9'}

soLike = []
for i in numbers:
    if str(i)[-1] in chu_so_thich:
        soLike.append(i)

soLike.sort()

print(len(soLike))
print(" ".join(map(str, soLike)))
    

