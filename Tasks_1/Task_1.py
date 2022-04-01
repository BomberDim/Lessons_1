#Даны два числа. Найти среднее арифметическое и среднее геометрическое их модулей.

import math

a = math.fabs(float(input('Введите а: ')))
b = math.fabs(float(input('Введите b: ')))

mean_arif = ((a + b) / 2)
mean_geom = math.sqrt(a * b)

print('Cреднее арифметическое: ',mean_arif)
print('Cреднее геометриеское: ',mean_geom)

#Просто для интереса

import statistics

listnumbers = [5, 6]

print ('Cреднее арифметическое 2: ',statistics.mean(listnumbers))
