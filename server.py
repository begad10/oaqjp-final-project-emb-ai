from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion_detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    else:
        return (
            f"For the given statement analyze is:,  "
            f"'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']}, "
            f"'sadness': {response['sadness']}, "
            f"The dominant emotion is {response['dominant_emotion']}"
        )
        
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    