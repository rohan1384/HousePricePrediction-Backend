from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model once at startup
model = joblib.load("D:\\Python\\HousePrice\\house_price_model.pkl")

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Extract request parameters
        medInc = float(request.args.get('medInc'))
        houseAge = float(request.args.get('houseAge'))
        aveRooms = float(request.args.get('aveRooms'))
        aveOccup = float(request.args.get('aveOccup'))

        # Prepare data for prediction
        feature_names = ["MedInc", "HouseAge", "AveRooms", "AveOccup"]
        input_data = pd.DataFrame([[medInc, houseAge, aveRooms, aveOccup]], columns=feature_names)

        # Predict house price
        predicted_price = model.predict(input_data)[0]

        return jsonify({"predictedPrice": predicted_price})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
