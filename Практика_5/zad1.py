capitals = {'Japan': 'Tokyo', 'U.S.A.': 'Washington D.C.', 'Russia': 'Moscow', 'DPRK': 'Pyongyang', 'Denmark': 'Copenhagen'}
print('Все ключи со значениями:')
for key in capitals:
    print(key, '-', capitals[key])
print(capitals['Japan'])
list_capitals = list(capitals.keys())
list_capitals.sort()
print('А теперь в алфавитном порядке:')
for i in list_capitals:
    print(i, '-', capitals[i])