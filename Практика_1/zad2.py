seat=int(input('Введите номер своего места '))
if seat in range(1, 36):
    if seat % 2 == 0:
        print('Ваше место в купе, верхняя полка', seat)
    else:
        print('Ваше место в купе, нижняя полка', seat)
elif seat in range(37, 54):
    if seat % 2 == 0:
        print('Ваше весто сбоку, верхняя полка', seat)
    else:
        print('Ваше весто сбоку, нижняя полка', seat)
else:
    print('Такого места нет')
#com1
