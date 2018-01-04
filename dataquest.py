file = open('test.csv', 'r')
data = file.read()
# print(data)
rows = data.split('\n')
# print(rows)
names = []
for row in rows:
    split_row = row.split(',')
    names.append(split_row)
print(names)
