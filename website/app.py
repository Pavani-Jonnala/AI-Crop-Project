from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained crop model
crop_model = joblib.load("../models/crop_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    state = request.form["state"]
    district = request.form["district"]
    area = request.form["area"]

    # Current agricultural input values
    # These will be connected to actual location data in the next stage.
    temperature = 28.0
    humidity = 75.0
    rainfall = 210.0

    nitrogen = 90
    phosphorus = 42
    potassium = 43
    ph = 6.5

    # Prepare input for ML model
    crop_input = [[
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    ]]

    # Actual ML prediction
    predicted_crop = crop_model.predict(crop_input)[0]

    analysis = {
        "temperature": f"{temperature} °C",
        "humidity": f"{humidity} %",
        "rainfall": f"{rainfall} mm",

        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
        "ph": ph,

        "flood_risk": "High",

        "crop": predicted_crop,

        "fertilizer": "Recommended based on soil condition",

        "solution": (
            f"{predicted_crop} is recommended based on the "
            "current agricultural conditions. Flood-tolerant "
            "varieties and proper water management can help "
            "reduce climate-related crop losses."
        )
    }

    return render_template(
        "result.html",
        state=state,
        district=district,
        area=area,
        analysis=analysis
    )


if __name__ == "__main__":
    app.run(debug=True)