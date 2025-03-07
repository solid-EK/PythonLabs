colors = input('Введите два основных цвета для получения нового: красный, синий или жёлтый ')
if 'синий' in colors.lower() and 'красный' in colors.lower():
    print('Вы получили фиолетовый!\nЭкзотично...')
elif 'жёлтый' in colors.lower() and 'красный' in colors.lower():
    print('Вы получили оранжевый!\nКак мандарин...')
elif 'жёлтый' in colors.lower() and 'синий' in colors.lower():
    print('Вы получили зелёный!\nМой любимый <3...')
else:
    print('Вы ввели не тот цвет 8(')

