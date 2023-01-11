import pandas as pd
from fuzzywuzzy import process
import sys
import const


def preprocess_polish_words():
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")

    polish_words = pd.read_csv('dictionaries/polish_words.txt', delimiter='=', header=0)
    polish_words = polish_words.sort_values(by=['freq'], ascending=False)
    polish_words = polish_words.drop_duplicates(subset=['word'])
    print(polish_words)

    word = []
    freq = []
    profanity = []
    hr = []

    index = 0
    print('start')
    for token in polish_words.values:
        index += 1
        if index > 50:
            break
        print(index, token[0])
        highest_ratio = process.extractOne(token[0], const.vulgarism_tuple)
        word.append(token[0])
        freq.append(token[1])
        profanity.append(highest_ratio[0])
        hr.append(highest_ratio[1])
    print('end')
    polish_words_clear = pd.DataFrame({'word': word, 'freq': freq, 'profanity': profanity, 'hr': hr})
    polish_words_clear.to_csv('dictionaries/final.csv', encoding='utf-8')
    print(polish_words_clear)


# preprocessed_polish_words = pd.read_csv('dictionaries/final.csv', delimiter=',', header=0)
# print(len(preprocessed_polish_words.query('hr >= 90')), preprocessed_polish_words.query('hr >= 90'))
# words_similar_to_profanities = preprocessed_polish_words.query('hr >= 75')
# words_similar_to_profanities.to_csv('dictionaries/words_similar_to_profanities.csv', encoding='utf-8', index=False)
# print(len(words_similar_to_profanities.query('hr >= 95')), words_similar_to_profanities.query('hr >= 95'))
# words_similar_to_profanities = words_similar_to_profanities.query('hr < 95')
# words_similar_to_profanities.to_csv('dictionaries/words_similar_to_profanities.csv', encoding='utf-8', index=False)

# words_similar_to_profanities = pd.read_csv('dictionaries/words_similar_to_profanities.csv', delimiter=',', header=0)
# with open("test.txt", "a", encoding='utf-8') as file:
#     file.write('whitelist = (\n')
#     for word in words_similar_to_profanities.values:
#         file.write(f'\t\"{word[1]}\",\n')
#     file.write(')')


