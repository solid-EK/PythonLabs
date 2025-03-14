def sub100(n):
    try:
        return n / 100
    except TypeError:
        return 'Введите число'
    except ZeroDivisionError:
        return 0


print(sub100(4))
print(sub100(0))
print(sub100(33))
print(sub100('Слово'))
