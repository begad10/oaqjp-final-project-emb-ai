"""
Flask server for emotion detection application.
This module handles the web interface and API requests for analyzing emotions in text.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyzes the emotion of the provided text and returns the result in the required format.
    Handles cases where the dominant_emotion is None.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    # Analyze emotion
    response = emotion_detector(text_to_analyze)

    # Handle cases where dominant_emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response as requested
    formatted_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    """
    Renders the index.html page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    app.run(host='0.0.0.0', port=5000, debug=True)
