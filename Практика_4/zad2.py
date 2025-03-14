num = [1,2,3,4,4,5,5,5,6,7,8,9,0]
repeat = {}
for x in num:
    if num.count(x) > 1:
        repeat[x] = num.count(x)
print('Число и количество повторений\n', repeat)
#print(*filter(lambda x: num.count(x) > 1, num))