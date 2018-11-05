text = str(input("Введите текст:"))
text += ' '
print('Слов:', text.count(' '))
print('Средняя длина предложения в словах:', text.count(' ') / text.count('.'))
