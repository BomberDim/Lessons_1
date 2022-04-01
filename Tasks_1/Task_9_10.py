#Треугольник задан координатами своих вершин. Найти периметр и площадь треугольника.

import math

x1 = (float(input('Введите x1: ')))
x2 = (float(input('Введите x2: ')))
x3 = (float(input('Введите x3: ')))

y1 = (float(input('Введите y1: ')))
y2 = (float(input('Введите y2: ')))
y3 = (float(input('Введите y3: ')))

a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

P = a + b + c

Sabc = (((x2 - x1) * (y3 - y1)) - ((x3 - x1) * (y2 - y1))) / 2

print('периметр треугольника: ', P)
print('площадь треугольника: ', Sabc)

#Выпуклый четырехугольник задан координатами своих вершин. Найти площадь этого четырехугольника
#как сумму площадей треугольников.

x1 = (float(input('Введите x1: ')))
x2 = (float(input('Введите x2: ')))
x3 = (float(input('Введите x3: ')))
x4 = (float(input('Введите x4: ')))

y1 = (float(input('Введите y1: ')))
y2 = (float(input('Введите y2: ')))
y3 = (float(input('Введите y3: ')))
y4 = (float(input('Введите y4: ')))

a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
d = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)
t = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

Sabc = (((x2 - x1) * (y3 - y1)) - ((x3 - x1) * (y2 - y1))) / 2

p = (t + d + c) / 2

Scdt = math.sqrt(p * (p - t) * (p - d) * (p - c))


print(f'площадь четырехугольника: {Sabc + Scdt}')