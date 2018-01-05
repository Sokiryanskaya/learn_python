import math
p = int(input())
x = int(input())
y = int(input())
k = int(input())
vklad = x*100+y
sum_vklad = vklad
for i in range(0, k):
    sum_vklad = sum_vklad * p/100 + sum_vklad
print(math.floor(sum_vklad // 100), round((sum_vklad % 100)))
