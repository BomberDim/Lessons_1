#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

"""Провести исследование биквадратного уравнения a,x4+b,x2+c=0 (a≠0),
где a, b и c - действительные числа.
Если действительных корней нет, то об этом должно быть выдано сообщение,
иначе должны быть выданы 2 или 4 действительных корня."""

if __name__ == '__main__':

    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))

    if a == 0:
        if b != 0:
            if c == 0:
                print("x=0")
            else:
                if c / b < 0:
                    x1 = sqrt(-(c/b))
                    x2 = -sqrt(-(c/b))
                    print(f'x1= {x1}', f'x2= {x2}')
                else:
                    print('Нет решений')
        else:
            if c != 0:
                print('Нет решений')
            else:
                print('x любое')
    else:
        d = sqrt(b * b) - 4 * a * c
        if d < 0:
            print('Нет решений')
        else:
            D = sqrt(d)
            y1 = (-b + D) / 2/a
            y2 = (-b - D) / 2/a
            if y1 > 0:
                x1 = sqrt(y1)
                x2 = -sqrt(y2)
                print(f'x1= {x1}', f'x2= {x2}')
            if y2 > 0:
                x3 = sqrt(y2)
                x4 = -sqrt(y2)
                print(f'x3= {x3}', f'x4= {x4}')



