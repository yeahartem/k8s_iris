from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('iris_model.joblib') # поправить на загрузку из mlflow

@app.route('/', methods=['GET'])
def heath():
    return jsonify({'status': 'ready', 'message':'IRIS ML MODEL'}), 200
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'no data'}), 400
        features = np.array([
            data.get('sepal_length', 0),
            data.get('sepal_width', 0),
            data.get('petal_length', 0),
            data.get('petal_width', 0),
        ]).reshape(1, -1)
        prediction = model.predict(features)
        probability = model.predict_proba(features)

        classes = ['setosa', 'versicolor', 'virgin']
        predicted_class = classes[prediction[0]]

        return jsonify({
            'prediction': predicted_class,
            'class_id': int(prediction[0]),
            'probabilities': {
                classes[i]: float(probability[0][i])
                for i in range(len(classes))
            }
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)
