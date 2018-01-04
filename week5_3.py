n = int(input())
for num in range(10 ** n - 1, 10 ** (n - 1)-1, -2):
    if num % 2:
        print(num, end=' ')
