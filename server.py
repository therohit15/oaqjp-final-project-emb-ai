from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotiondetector():
    text_to_detect = request.args.get('textToAnalyze', '')
    response = emotion_detector(text_to_detect)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!', 400
    
    else:
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