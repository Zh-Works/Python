#!/usr/bin/python3.5
val=input('Введите через пробел значения A, B, C\n').split(' ')
values=list(map(lambda x: float(x), val))
print('Минимальное значение из введенных{}'.format(min(values)))

print('Максимальное значение из введенных{}'.format(max(values)))

