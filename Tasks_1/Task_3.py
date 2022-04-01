import math

a = float(input ("Введите a:"))
b = float(input("Введите b:"))
c = float(input("Введите c:"))

p = (a + b + c) / 2
S = math.sqrt((p * (p-a) * (p-b) * (p-c)))

print(S)