#!/usr/bin/python3.5
import random
l=int(input('Введите длину массива\n'))
mas=list(map(lambda x: random.randint(0, 51),range(0, l) ))
print(mas)
a=0
for i in range(0, len(mas)):
    if i%2==1:
        a=mas[i]
        mas[i]=mas[i-1]
        mas[i-1]=a
print(mas)
