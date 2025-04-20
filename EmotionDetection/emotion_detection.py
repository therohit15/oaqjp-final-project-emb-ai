import requests
import json

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json =obj, headers = header)

    if response.status_code == 400:
        emotion_scores = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotion_scores

    formatted_response = response.json()
    emotionPredictions = formatted_response["emotionPredictions"]
    emotion = emotionPredictions[0]
    emotions = emotion["emotion"]
    emotion_scores = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0)
    }

    emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)
    return emotion_scores
    
        
    
    