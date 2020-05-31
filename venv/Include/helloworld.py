import random
arg1 = int(input('Введите длину списка: '))
arg2 = int(input('Введите максимальное значение элемента списка: '))

def create_list(arg1,arg2):
    new_list = list()
    while(len(new_list) < arg1):
        new_list.append(random.randint(0,arg2 + 1))
    print(new_list)

create_list(arg1,arg2)