import requests
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

API_URL = "https://countriesnow.space/api/v0.1/countries/capital"

# Global variable to store the current random country.
current_country = {}

def get_countries():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json().get("data", [])
    return []

@app.route('/get_country', methods=['GET'])
def get_country():
    global current_country
    countries_data = get_countries()
    current_country = random.choice(countries_data) if countries_data else {}
    return jsonify({"country": current_country.get("name", "Unknown")})

@app.route('/check_capital', methods=['POST'])
def check_capital():
    """ Accepts a guessed capital and validates it """
    data = request.get_json()
    guessed_capital = data.get("capital", "").strip()
    correct_capital = current_country.get("capital", "")

    # If the country API data has no capital recorded.
    if not correct_capital:
        return jsonify({
            "correct": False,
            "message": "This country does not have a recorded capital. Please try another country."
        })

    # If the user does not provide any guess.
    if not guessed_capital:
        return jsonify({
            "correct": False,
            "message": "You did not provide a guess. Please enter a capital."
        })

    # Verify the guess. 
    if guessed_capital.lower() == correct_capital.lower():
        return jsonify({"correct": True, "message": "Well done!"})
    else:
        return jsonify({
            "correct": False,
            "message": f"Incorrect! The correct capital is {correct_capital}."
        })



if __name__ == '__main__':
    app.run(debug=True)
