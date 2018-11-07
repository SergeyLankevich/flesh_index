import localization
text = input(localization.text)

lower_text = text.lower()
sentences = text.count('.')
words = text.count(' ') + 1
syllables = lower_text.count(localization.vowel1) + lower_text.count(localization.vowel2) + lower_text.count(localization.vowel3) + \
            lower_text.count(localization.vowel4) + lower_text.count(localization.vowel5) + lower_text.count(localization.vowel6) + \
            lower_text.count(localization.vowel7) + lower_text.count(localization.vowel8) + lower_text.count(localization.vowel9) + \
            lower_text.count(localization.vowel10)

if sentences == 0:
    print(localization.exception)
else:
    asl = round(words / sentences, 2)
    asw = round(syllables / words, 2)
    print(localization.syllables, syllables)
    print(localization.words, words)
    print(localization.average_sentence_length, asl)
    print(localization.number_of_syllables_per_word, asw)

flesh_index = round(206.835 - (1.3 * asl) - (60.1 * asw), 4)
print(localization.index, flesh_index)
