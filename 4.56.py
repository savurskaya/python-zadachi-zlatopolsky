#савурская полина, задача 4.56
abcd = int(input())
a = (abcd % 10000) // 1000
b = (abcd % 1000) // 100
c = (abcd % 100) // 10
d = abcd % 10
if a == d and b == c:
    print('запись числа является симметричной')
else:
    print('запись числа не является симметричной')