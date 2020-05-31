a=int(input('Введите число 1: '))
b=int(input('Введите число 2: '))
v=int(input('Введите число 3: '))

def cycle(a,b,v):
    while a <= b:
        print(str(a) + ' Пока что нет')
        a = a + v
    else:
        a > b
        print('Дождались ' + str(a))

cycle(a,b,v) 