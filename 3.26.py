#савурская полина, задача 3.26

abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
print(a,b,c, sep='')
print(a,c,b, sep='')
print(b,a,c, sep='')
print(b,c,a, sep='')
print(c,a,b, sep='')
print(c,b,a, sep='')