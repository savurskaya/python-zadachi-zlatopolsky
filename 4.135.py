#савурская полина, задача 4.135
m = int(input())
if 1 <= m <= 2 or m == 12:
    print('зима')
elif 3 <= m <= 5:
    print('весна')
elif 6 <= m <= 8:
    print('лето')
elif 9 <= m <= 11:
    print('осень')
else:
    print('неправильно введен месяц')