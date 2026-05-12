def multiplicativePersistence(num):
    r = 0
    while num >= 10:
        s = 1
        for digit in str(num):
            s *= int(digit)
        num = s
        r += 1
    return r