import localization
text = input(localization.text)

lower_text = text.lower()
sentences = text.count('.')
words = text.count(' ') + 1
syllables = lower_text.count(localization.vowel1) + lower_text.count('е') + lower_text.count('ё') + \
            lower_text.count('и') + lower_text.count('о') + lower_text.count('э') + lower_text.count('у') \
            + lower_text.count('ю') + lower_text.count('ы') + lower_text.count('я')

if sentences == 0:
    print('localization.exception')
else:
    asl = round(words / sentences, 2)
    asw = round(syllables / words, 2)
    print(localization.syllables, syllables)
    print(localization.words, words)
    print(localization.average_sentence_length, asl)
    print(localization.number_of_syllables_per_word, asw)

flesh_index = round(206.835 - (1.3 * asl) - (60.1 * asw), 4)
print(localization.index, flesh_index)
