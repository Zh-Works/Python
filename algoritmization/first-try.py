#!/usr/bin/python3
value=input('Введите зарплату:')
stav=input('Введите величину налога:')

nal=float(value)*float(stav)/100
salary=float(value) - nal

print('На руки вы получите {0},\nПри этом размер вычета будет равняться {1}'.format(salary, nal))
