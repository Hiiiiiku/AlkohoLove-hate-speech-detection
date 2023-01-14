# AlkohoLove-hate-speech-detection

## Setup
`pip install -r requirements.txt` to install requirements.

`docker-compose up --build -d`  to run app.
## Docs
Docs are avaliable on
`http://localhost:8008/docs`.

## Detection methods
Service uses two methods to clasify comment as harmfull.
 - dict method
 
 Dict method has two dictionaries. Black and white list. Black list contains polish vulgarisms. 
 White list contains non harmfull polish words that have been mistaken as harmfull. It was created from 40000 most popular words.
 For every word in review service counts Levenshtein distance. If word is classified as harmfull system checks if it is in white list. If it is, word in not hramfull. If not, word is harmfull. 
 - neural network
 
 This metod uses cnn model that was learning on 10000 polsih posts from twitter. 
