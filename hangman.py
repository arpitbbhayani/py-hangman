# Hangman
#
# Installing required packages
#     $ pip install flask flask-cors
#
# Run
#     $ python hangman.py
#

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


TOTAL_CHANCES = 6

# Make your changes in the function below
def check(word, guesses, guess):
    """The function accepts following arguments

    - word: the word to be guessed
    - guesses: list of characters (as strings) already guessed
    - guess: the current character (as strings) guessed

    The function should return the following

    - masked_word: the word that has been guessed till now.
          The letters not yet guessed should be `-`
    - chances_left: number of chances left after this
    - game_won: Boolean value that represents if the game is won
    - game_lost: Boolean value that represents if the game is lost

    For example:
      For example:
        If the word to be guessed is "hangman", and in this turn the player
        has guessed "g" and previous guesses were z, q, r, a, m

      The function would return
      - "_a_gma_"
      - 5
      - False
      - False
    """
    return "-" * len(word), TOTAL_CHANCES, False, False


@app.route('/check', methods=['POST'])
def api_check():
    """This API exposes a HTTP POST method to check the state of the game

    API via cURL request looks like this:

    curl -XPOST http://localhost:9000/check -H 'Content-Type: application/json' -d '{"word": "hangman", "guesses": ["a"], "guess": "x"}'
    """
    body = request.json
    masked_word, chances_left, game_won, game_lost = check(body['word'], body['guesses'], body['guess'])
    return jsonify({
      "masked_word": masked_word,
      "chances_left": chances_left,
      "game_won": game_won,
      "game_lost": game_lost,
    })


app.run(host="0.0.0.0", port=9000)
