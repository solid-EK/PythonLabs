import random
error_count = 0
success_count = 0
while error_count < 3:
    numbers = [random.randint(1, 25), random.randint(1, 25)]
    task = str(numbers[0]) + ' + ' + str(numbers[1]) + ' = '
    answer = int(input(task))
    if answer == numbers[0] + numbers[1]:
        print('Correct')
        success_count += 1
    else:
        print('Fault')
        error_count += 1
print('Game over\nYour score:', success_count)
