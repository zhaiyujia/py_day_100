# sum = 0
# for i in range(100):
#     sum += i
#
# print(sum)
#
# for i in range(1, 100):
#     print(i)
#
# for i in range(1, 100, 10):
#     print(i)
# import random
#
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入: '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
#
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')


for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
