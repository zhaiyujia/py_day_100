t = ('zhai', 29, True, '北京')
print(t)
print(t[0])
print(t[3])
print('--------------------')
for member in t:
    print(member)

# t[0] = '王大锤'
# print(t)
print('--------------------')
t = ('王大锤', 20, True, '云南昆明')
print(t)
print('--------------------')
person = list(t)
print(person)
person[0] = '李小龙'
person[1] = 25
print('--------------------')
print(person)
print('--------------------')

fruits_list = ['apple', 'banana', 'orange']
t = tuple(fruits_list)
print(t)