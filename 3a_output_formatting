import requests
import json

"""
URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyze } }

"""
def emotion_detector(text_to_analyze):
    
    # defining headers and json input
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text":text_to_analyze}}
    response = requests.post(url, json = myobj, headers=headers)
    res_dict = json.loads(response.text)

    # extracting emotions anger, disgust, fear, joy and sadness, along with their scores
    emotions = res_dict['emotionPredictions'][0]['emotion']

    # using python max() to find highest score 
    dominant_emotion = max(emotions, key=emotions.get)

    # assigning emotions scores to variables
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

