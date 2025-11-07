from flask import Flask
from flask.json import jsonify
import random

app = Flask(__name__)

def life():
    fin = open("mongo_crud\\quote.txt", "r")
    random_line = random.randint(0, 2)
    quote = fin.readlines()[random_line]
    return jsonify(quote[0:-1])

if __name__ == "__main__":
    app.run(debug=True)