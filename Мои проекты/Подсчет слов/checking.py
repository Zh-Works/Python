#!//usr/bin/python3.5
#-*- codig:UTF-8 -*-
"""Программа раз
"""
from sys import argv

def engine(file):
    return len(file)

def clearing(what, where):
        while what in where:
            where.remove(what)
    
    
def statistic(array):
    i=0
    print('Статистика по элементам:')
    while len(array) !=0:
        item=array[0]
        print('Элемент',  item,'встречается в тексте', array.count(item),  'раз')
        clearing(item, array)
        i+=1
        print(array)
        continue
    print('В тексте насчиталось', i , 'разных элементов')
    
def normalize(string):
    print(string)
    for i in [',', '.', ':', '!',  '?', ';',  '', '(', '\n',')']:
        string=string.replace(i, '')
    print(string.split())
    return(string.split())
if argv[1] =='':
    print ('Необходимо указать анализируемый файл')
    exit()
else:
    filename=argv[1]
    
fd=open(filename, 'r')
text=normalize(fd.read())
print ('Длина текста составляет', engine(text),' знаков')
statistic(text)
fd.close
