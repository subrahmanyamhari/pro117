from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Get Input Text from POST Request
    input_text = request.json.get("text")

    if not input_text:
        # Response to send if the input_text is undefined
        response = {
            "status" : "ERROR",
            "message" : "enter in a proper. way couldn't be processed",
        }
        return jsonify(response)
        # Response to send if the input_text is not undefined
    else :
        predict_emotion = predict(input_text)
        response = {"status": "success",
                    "data":{"predict_emotion":predict_emotion}}

        # Send Response         
        for key, value in emo_code_url.items():
            if value[0] == predict_emotion:
                print(predict_emotion)
        return predict_emotion
app.run(debug=True)