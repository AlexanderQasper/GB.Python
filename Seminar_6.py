def calc_1(stroka) -> list:
    res = []
    n = 0
    for i in range(len(stroka)):
        if stroka[i] in ('+', '-', '*', '/'):
            res.append(stroka[n:i])
            res.append(stroka[i])
            n = i + 1
    res.append(int(stroka[i:]))
    return res

print(calc_1('5 * 6 / 7'))

