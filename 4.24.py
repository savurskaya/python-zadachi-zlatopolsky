#савурская полина, задача 4.23

n = int(input())
if n % 2 == 0:
    print('число', n, 'четное')
else:
    print('число', n, 'нечетное')
if n % 10 == 7:
    print('число оканчивается цифрой 7')
else:
    print('число не оканчивается цифрой 7')
