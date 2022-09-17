'''
练习1：输入一个正整数判断是不是素数。

提示：素数指的是只能被1和自身整除的大于1的整数。
'''

from math import sqrt
num = int(input('请输入一个整数：'))
end = int(sqrt(num))
is_prime = True

for x in range(2, end + 1):
    if num % 2 == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

