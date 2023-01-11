from fastapi import APIRouter, status, Body, HTTPException

from src.detection_methods import dict_method, neural_network_method

profanity_router = APIRouter(prefix='/hate_speech_detection', tags=['hate-speech-detection'])


@profanity_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    summary='Detect hate speech and profanity in review'
)
def detect_hate_speech(
    review: str = Body(...)
):
    print(review)
    if dict_method(review) or neural_network_method(review):
        print(True)
        return True
    print(False)
    return False
