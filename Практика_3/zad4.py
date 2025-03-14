def lucky_ticket(number):
    digits = [int(d) for d in number]
    mid = len(digits)//2
    first = sum(digits[:mid])
    last = sum(digits[mid:])
    return first == last


print(lucky_ticket('3322'))
print(lucky_ticket('385916'))