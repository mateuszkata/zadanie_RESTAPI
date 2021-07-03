from flask import Flask, jsonify, request
from collections import Counter

app = Flask(__name__)

words = ["apple", "banana", "chair"]


@app.route("/wordlist", methods=['GET'])
def get():
    return jsonify({'list_of_words': words})


@app.route("/wordlist", methods=['POST'])
def create():
    word = request.data
    words.append(word)
    return jsonify({'list_of_words': words}), 202


@app.route("/wordlist/<word>", methods=['DELETE'])
def delete(word):
    words.remove(word)
    return jsonify({'result': True})


@app.route("/wordlist/unique", methods=['GET'])
def unique(words):
    list_of_unique_words = set()
    for word in words:
        list_of_unique_words.append(word)
    return jsonify({'list_of_words': list_of_unique_words})


@app.route("/wordlist/count", methods=['GET'])
def count():
    counts = dict(Counter(words))
    return jsonify({'counter': counts})


if __name__ == '__main__':
    app.run(debug=True)
