import sys

f = [x for x in range(1, 10)]
print(f)

f = [x + y for x in 'ABCD' for y in '1234567']
print(f)

f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))
print(f)

f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
list1 = []
for val in f:
    list1.append(val)
print(list1)










