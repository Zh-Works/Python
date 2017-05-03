#!/usr/bin/python3.5
from datetime import date
now=str(date.today())
nowlist=str(date.today()).split('-')
rusnow='/'.join(nowlist)
god=str(date.today()).split('-')[0]
if int(god)%4==0:
    print('Сейчас високосный год')
print('Сейчас идет {} век'.format(int(god)//100 +1))
