word = input('Проверка на редкость слова\nВведите ваше слово:')
if word.isalpha():
    if 'ф' in word.lower():
        print('Ого! Это редкое слово!')
    else:
        print('Эх, это не очень редкое слово...')
else:
    print('Введите слово')