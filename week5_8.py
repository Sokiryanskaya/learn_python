n = int(input())
s = 0
j = 1
for i in range(1, n+1):
    j = j * i
    s = s + j
print(s)
