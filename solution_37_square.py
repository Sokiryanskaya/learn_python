f = open('test.csv', 'r')
names = f.read()
names_list = names.split('\n')
test = []
for i in names_list:
    list_1 = i.split(',')
    test.append(list_1)
test2 = []
for rows in test:
    list_2 = rows[1]
    test2.append(list_2)
print(test)
print(test2)
