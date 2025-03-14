import random
MD25 = ['Смирнов', 'Геровская', 'Мусаев', 'Баранов', 'Смирнов', 'Калабишка', 'Алёхин', 'Гаража', 'Кондрашёва', 'Эрмиш']
MD20 = ['Кондрашкин', 'Субботин', 'Овчинников', 'Шафиков', 'Милых', 'Писарев', 'Игнатьев', 'Рыжов', 'Попова', 'Каюмов']
team = []
ran = list(range(0, 10))
random.shuffle(ran)
for l in range(5):
    team.append(MD20[int(ran[l])])
for l in range(5):
    team.append(MD25[int(ran[l])])
print(', '.join(MD25),'\n',', '.join(MD20), '\n',', '.join(team), '\n', len(team),'\n', ', '.join(sorted(team)))
if 'Смирнов' in team:
    print(team.count('Смирнов'))