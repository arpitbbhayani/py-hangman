# Hangman UI
#
# Installing required packages
#     $ pip install flask
#
# Run
#     $ python ui.py
#

from flask import Flask

app = Flask(__name__, static_url_path='/')


@app.route('/')
def index():
    return app.send_static_file('./index.html')


app.run(host="0.0.0.0", port=3000)
