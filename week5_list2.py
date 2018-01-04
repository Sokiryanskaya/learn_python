# Выведите все четные элементы списка.
n = list(map(int, input().split()))
print(*(i for i in n if i % 2 == 0))
# for i in n:
#     if i % 2 == 0:
#         print(i, end=' ')
