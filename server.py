"""
This module contains a Flask application for emotion detection using Watson NLP API.
It provides a web interface and an API endpoint for analyzing emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Render the main page with the interface for emotion detection.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotiondetector():
    """
    Detect emotions in a given text using the emotion_detector function.
    """
    text_to_detect = request.args.get('textToAnalyze', '')
    response = emotion_detector(text_to_detect)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!', 400
    response_message = (
        f"For the given statement, the system response is 'anger': "
        f"{response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )
    return response_message

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)
