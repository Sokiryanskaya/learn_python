# Даны два четырёхзначных числа A и B. Выведите все
# четырёхзначные числа на отрезке от A до B,
# запись которых является палиндромом.
A = int(input())
B = int(input())
for i in range(A, B+1):
    if str(i) == str(i)[::-1] and len(str(i)) == 4:
        print(i, sep='\n')
    else:
        pass
print()
