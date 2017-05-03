#!/usr/bin/python3.5

print('Давай узнаем, пройдет ли коробка в дверь')
razd=input('Символ-разделитель размеров')
while True:    
    door_raw=input('Размер двери\n')
    door=list(map(lambda x: float(x), door_raw.split(razd)))
    box_raw=input('Размер коробки\n')
    box=list(map(lambda x: float(x), box_raw.split(razd)))
    if (box[0]<door[0] and box[1]<door[1]) or (box[1]<door[0] and box[0]<door[1]):
       print('Войдет')
    elif (box[1]<door[0] and box[2]<box[1]) or (box[2]<door[0] and box[1]<door[1]):
        print('Войдет')
    elif (box[0]<door[0] and box[2]<box[1]) or (box[2]<door[0] and box[0]<door[1]):
        print('Войдет')
    else:
        print('Не пролезет')

    cont=input('Хочешь еще повписывать коробки в двери? Да?\n')
    if cont=='Да' or cont=='да':
        continue
    else:
        break
