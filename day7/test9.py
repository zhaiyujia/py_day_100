set1 = {1, 2, 3}
set2 = {1, 43, 5}
set3 = {1, 2}
# 交集
print(set1 & set2)
# 并集
print(set1 | set2)
# 左差集
print(set1 - set2)
print(set2 - set1)
# {2, 3, 5, 43}
print(set1 ^ set2)

print(set2 <= set1)
print(set3 <= set1)
print(set1 >= set2)
print(set1 >= set3)