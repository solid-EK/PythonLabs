import random
nums = []
for i in range(6):
    nums.append(str(random.randint(1, 100)))
guess = input('Отгадайте число ')
if guess.isdigit():
    if guess in nums:
        print('Ваше число:', guess, 'Загаданные числа:', ', '.join(nums), '\nПоздравляю! Вы угадали число!')
    else:
        print('Ваше число:', guess, 'Загаданные числа:', ', '.join(nums), '\nТакого числа нет')
else:
    print('Введите число')