# Найдите наибольшее значение в списке и индекс последнего элемента,
# который имеет данное значение за один проход по списку,
# не модифицируя этот список и не используя дополнительного списка.
n = list(map(int, input().split()))
max_1 = 0
index = n[0]
for ind, max_2 in enumerate(n):
    if max_2 > max_1 or max_2 == max_1:
        max_1, index = max_2, ind
print(max_1, index)
