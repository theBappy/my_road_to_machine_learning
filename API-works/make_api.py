from flask import Flask
from flask.json import jsonify
import random

app = Flask(__name__)

@app.route("/")
def life():
    fin = open("API-works\\quote.txt")
    random_line = random.randint(0,2)
    quote = fin.readlines()[random_line]
    return jsonify(quote[0:-1])

if __name__ == "__main__":
    app.run(debug=True)