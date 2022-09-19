# list1 = [1, 3, 5, 7, 100]
# print(list1)
#
# list2 = ['hello'] * 3
# print(list2)
#
# print(len(list1))
# print(list1[0])
# print(list1[4])
# print(list1[-1])
# print(list1[-3])
#
# list1[2] = 300
# print(list1)
#
# for index in list1:
#     print(index, end=' ')
#
# print()
#
# for index in range(len(list1)):
#     print(list1[index], end=' ')
#
# for index, elem in enumerate(list1):
#     print(index, elem)

list1 = [1, 3, 5, 7, 100]
list1.append(200)
list1.insert(1, 300)
print(list1)
list1 += [1000, 2000]
print(list1)
print(len(list1))

if 3 in list1:
    list1.remove(3)
print(list1)
if 1234 in list1:
    list1.remove(1234)
print(list1)
list1.pop(0)
print(list1)
list1.pop(len(list1) - 1)
print(list1)
list1.clear()
print(list1)











