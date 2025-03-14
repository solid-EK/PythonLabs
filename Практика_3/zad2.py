stro = ''
word = input('Введите слово')
while word != 'stop':
    stro = stro + word + ' '
    word = input('Введите слово')
print(stro)