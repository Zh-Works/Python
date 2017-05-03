#!/usr/bin/python3.5
import random
l=int(input('Введите длину массива\n'))
mas=list(map(lambda x: random.randint(0, 51),range(0, l) ))
print(mas)
a=mas[len(mas)-1]
for i in range( len(mas)-1, 0, -1):
    a=mas[i]
    mas[i]=mas[i-1]
mas[0]=a
print(mas)
