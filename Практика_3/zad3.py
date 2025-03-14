def magic_number(date):
    try:
        day, month, year = map(int, date.split('.'))
        return day * month == year % 100
    except ValueError:
        return False


print(magic_number('02.11.2022'))
