#!/usr/bin/python3.5
import random
l=int(input('Введите длину массива\n'))
mas=list(map(lambda x: random.randint(-51, 51),range(0, l) ))
print(mas)
a=mas[len(mas)-1]
for i in range(0, len(mas)+2):
    if mas[i] < 0:
        kv=mas[i]**2
        mas.insert(i+1, kv)
print(mas)
