#савурская полина, задача 4.63
from math import sqrt
a = int(input())
b = int(input())
d = int(input())
c = sqrt(a**2 + b**2)
if d < c:
    print('голова пролезет в форточку')
else:
    print('голова не пролезет в форточку')