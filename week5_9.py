# Для настольной игры используются
# карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек
n = int(input())
card = [int(input()) for _ in range(n-1)]
for i in range(1, n+1):
    if i not in card:
        print(i)
