n = int(input('Сколько слов вы хотите ввести?'))
stro = ''
for i in range(n):
    word = input('Введите слово')
    stro = stro + word + ' '
print(stro)