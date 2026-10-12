
from flask import Flask, jsonify, request

app = Flask(__name__)

PROGRAMS = {
    "fat_loss": {
        "name": "Fat Loss",
        "workout": "Strength training and cardio",
        "calorie_factor": 22,
    },
    "muscle_gain": {
        "name": "Muscle Gain",
        "workout": "Progressive strength training",
        "calorie_factor": 35,
    },
    "beginner": {
        "name": "Beginner",
        "workout": "Full-body beginner training",
        "calorie_factor": 26,
    },
}


@app.route("/")
def home():
    return jsonify({
        "application": "ACEest Fitness & Gym",
        "status": "running",
        "message": "Welcome to ACEest Fitness!",
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/programs")
def get_programs():
    return jsonify(PROGRAMS), 200


@app.route("/calculate-calories", methods=["POST"])
def calculate_calories():
    data = request.get_json(silent=True) or {}

    program = data.get("program")
    weight = data.get("weight")

    if program not in PROGRAMS:
        return jsonify({"error": "Invalid fitness program"}), 400

    if isinstance(weight, bool) or not isinstance(weight, (int, float)):
        return jsonify({"error": "Weight must be a number"}), 400

    if not 1 <= weight <= 500:
        return jsonify({"error": "Weight must be between 1 and 500 kg"}), 400

    calories = round(weight * PROGRAMS[program]["calorie_factor"])

    return jsonify({
        "program": PROGRAMS[program]["name"],
        "weight": weight,
        "estimated_calories": calories,
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
