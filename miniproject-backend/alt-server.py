from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/predict/stress', methods=['POST'])
def predict_stress_route():
    data = request.json
    text = data['text']
    # 🔁 Replace this with mock output
    response = {'Disorder Present': 'Stressed', 'Severity Score': 8.5}
    return jsonify(response)

@app.route('/predict/multiclass', methods=['POST'])
def predict_multiclass_route():
    data = request.json
    text = data['text']
    response = {'Disorder': 'moderate', 'Severity Score': 7.9}
    return jsonify(response)

@app.route('/predict/mental', methods=['POST'])
def detect_mental_illness_route():
    data = request.json
    text = data['text']
    # You can return a dummy disorder here
    response = {'mental_illness': 'Anxiety'}
    return jsonify(response)

@app.route('/recommendations', methods=['POST'])
def recommendations_route():
    data = request.json
    mental_disorder = data['mental_disorder']
    # Dummy recommendations
    response = {
        'recommendations': f"For {mental_disorder}, try journaling, therapy, and regular sleep."
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
