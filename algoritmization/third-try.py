p=int(input('Введите оценку:\n'))
if p<=0 or p>5:
        print('Это число не может быть оценкой')
if p==2 or p==1:
    print('Лентяй')
elif p==3:
    print('Можно лучше')
elif p==4:
    print('Почти молодец')
else:
    print('Молодец')
