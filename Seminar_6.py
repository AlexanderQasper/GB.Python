orig_text = 'марат карат забвение квартал абдоминальный абвер'
text1 = orig_text.split()

print(*filter(lambda x: 'абв' not in x, text1))