'''
输出100以内所有的素数。

说明：素数指的是只能被1和自身整除的正整数（不包括1）。
'''

for i in range(2, 100):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print("%d 是素数" % i)

# count = 0
# i = 4
# for j in range(1, i + 1):
#     if i % j == 0:
#         print(j)
#         count += 1
# if count == 2:
#     print("%d 是素数" % i)
