str1 = 'hello, world!'

print(len(str1))
print(str1.capitalize())
print(str1.title())
print(str1.upper())
print(str1.find('or'))
# print(str1.index('shit'))
print(str1.startswith('He'))
print(str1.startswith('hel'))
print(str1.endswith('!'))
print(str1.center(50, '*'))
print(str1.rjust(50, ' '))

str2 = 'abc123456'
print(str2.isdigit())
print(str2.isalpha())
print(str2.isalnum())
str3 = '  jackfrued@126.com 1'
print(str3)
print(str3.strip())

a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')
