"""
Emotion Detector Server Module

This module sets up a Flask server to detect emotions from provided text input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to detect the dominant emotion from the provided text.

    Retrieves the text to analyze from the request arguments, processes it using
    the emotion_detector, and returns a formatted response based on the detected emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return_val = "Invalid text! Please try again!"
    else:
        formatted_response = response.copy()
        formatted_response.popitem()
        response_str = str(formatted_response).replace('{', '').replace('}', '')
        return_val = (
            f"For the given statement, the system response is {response_str}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )

    return return_val


@app.route("/")
def render_index_page():
    """
    Renders the index HTML page.

    Serves the main page where users can input text for emotion detection.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
