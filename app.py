from flask import Flask, request, jsonify
from flask_cors import CORS  # type: ignore

app = Flask(__name__)
CORS(app)


@app.route("/bfhl", methods=["POST"])
def post_bfhl():
    try:
        data = request.json.get("data", [])
        user_id = "aakash_28112002"
        email = "az4058@srmist.edu.in"
        roll_number = "RA2111033010135"

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_alphabet = sorted(alphabets, key=lambda x: x.upper(), reverse=True)[:1]

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet,
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)})


@app.route("/bfhl", methods=["GET"])
def get_bfhl():
    return jsonify({"operation_code": 1})


if __name__ == "__main__":
    app.run(debug=True)
