

a=int(input('Введите число 1: '))
b=int(input('Введите число 2: '))
c= int(input('Введите число 3: '))
if a > b:
    print("Свершилось!")
elif b > a :
   print("Да ну!")
elif b == a :
   print("А если так?")
   a = a+b
   b = b-c
   if a > b:
       print("Свершилось!")
   elif b > a:
       print("Да ну!")
   elif b == a:
       print("А если так?")







