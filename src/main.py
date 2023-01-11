
from uvicorn import run
from fastapi import FastAPI

from src.hate_speech_detection_api import profanity_router


app = FastAPI(title='AlkohoLove-hate-speech-detection-service')

app.include_router(profanity_router)

if __name__ == '__main__':
    run('main:app', host='127.0.0.1', port=8008, reload=True)
