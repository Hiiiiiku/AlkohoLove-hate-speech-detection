import json
import re

from keras.preprocessing.text import tokenizer_from_json
from keras_preprocessing.sequence import pad_sequences
from fuzzywuzzy import process
from tensorflow import keras

from src.const import vulgarism_tuple, whitelist

cnn_model = keras.models.load_model('src/models/cnn_model')
print("cnn_model Loaded")

with open('src/models/tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)


def dict_method(text: str) -> bool:
    text = re.sub(
        r'\b\w{1,2}\b',
        ' ',
        text
    )
    text = (text.lower().split())
    for token in text:
        highest_ratio = process.extractOne(token, vulgarism_tuple)
        print(token, highest_ratio, highest_ratio[1])
        if highest_ratio[1] > 75:
            if token in whitelist:
                continue
            return True
    return False


def neural_network_method(text: str) -> bool:
    text = re.sub(
        r'[^\w\s]|[\d+]|\b\w{1,3}\b|[\s+]',
        ' ',
        text
    )
    text = ' '.join(text.split()).lower()
    xtext = tokenizer.texts_to_sequences([text])
    xtext = pad_sequences(xtext, maxlen=17)
    prediction = cnn_model.predict(xtext, verbose=1)
    print(prediction[0][0])
    return bool(round(prediction[0][0]))
