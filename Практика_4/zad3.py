days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
holidays = int(input('Сколько выходных на неделе вы хотите? '))
if 0 <= holidays <=7:
    print('Ваши выходные:', ', '.join(days[-holidays:]), '\nВаши РАБочие дни:', ', '.join(days[:-holidays]))
else:
    print('Введите число в пределах 7')