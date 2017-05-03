#!/usr/bin/python3.5
import random
l=int(input('Введите длину массива\n'))
mas=mas2=list(map(lambda x: random.randint(0, 51),range(0, l) ))
print(mas)
a=0
#for a in range(0, len(mas)):
while a<len(mas):
    for i in range(0, len(mas)-1):
        if mas[i]>mas[i+1]:
            b=mas[i+1]
            mas[i+1]=mas[i]
            mas[i]=b
    print(mas)
    a+=1
    input('')
#mas2.sort()
#print(mas2)

    
