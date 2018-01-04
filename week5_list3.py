# Найдите количество положительных элементов в данном списке.
n = list(map(int, input().split()))
# s = 0
# for i in n:
#     if i > 0:
#         s += 1
# print(s)
print(len(list(i for i in n if i > 0)))
