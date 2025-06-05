# guess_capital

Country Capital Guessing Game API

This is a simple Flask-based API that allows users to guess the capital city of a randomly selected country. It fetches real-world data from a public API (`https://countriesnow.space/api/v0.1/countries/capital`) and validates the user's guess.

---
 Installation Instructions

1. Clone the Repository
`
git clone https://github.com/harshvardhan30/guess_capital.git
cd guess_capital


2. (Optional) Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate


3. Install Required Dependencies
pip install -r requirements.txt

4. Run the Application
python app.py
The server will start on: http://127.0.0.1:5000



##API Endpoints:

1. GET /get_country
   - Description: Fetches a random country and stores it for capital validation.
   - curl:
     
     curl --location 'http://127.0.0.1:5000/get_country'

2. POST /check_capital
   - Description: Accepts a guessed capital and checks if it matches the selected country's capital.
   - Request body (JSON):
     {
       "capital": "YourGuess"
     }
   - curl:
     
     curl --location 'http://127.0.0.1:5000/check_capital' \
     --header 'Content-Type: application/json' \
     --data '{"capital": "Bridgetown"}'

Responses:

- For /get_country:
  {
    "country": "CountryName"
  }

- For /check_capital:

  Correct guess:
  {
    "correct": true,
    "message": "Well done!"
  }

  Incorrect guess:
  {
    "correct": false,
    "message": "Incorrect! The correct capital is CorrectCapitalname."
  }

  Missing guess:
  {
    "correct": false,
    "message": "You did not provide a guess. Please enter a capital."
  }

  No capital available for the country:
  {
    "correct": false,
    "message": "This country does not have a recorded capital. Please try another country."
  }


Testing Sequence
============================

Step 1 → Call:
curl --location 'http://127.0.0.1:5000/get_country'

Step 2 → Use the returned country name to guess its capital:
curl --location 'http://127.0.0.1:5000/check_capital' \
--header 'Content-Type: application/json' \
--data '{"capital": "YourGuess"}'
