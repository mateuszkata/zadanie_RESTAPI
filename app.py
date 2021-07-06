from flask import Flask, jsonify, request

app = Flask(__name__)

words = ["apple", "banana", "chair", "apple"]


@app.route("/wordlist", methods=['GET'])
def get():
    return jsonify({'list_of_words': words})


@app.route("/wordlist", methods=['POST'])
def create():
    word = request.get_json()['word']
    words.append(word)
    return jsonify({'list_of_words': words})


@app.route("/wordlist/<word>", methods=['DELETE'])
def delete(word):
    words.remove(word)
    return jsonify({'result': True})


@app.route("/wordlist/unique", methods=['GET'])
def unique():
    list_of_unique_words = set(words)
    return jsonify({'list_of_words': list(list_of_unique_words)})


@app.route("/wordlist/<word>", methods=['GET'])
def count(word):
    return jsonify({'counter': words.count(word)})


if __name__ == '__main__':
    app.run(debug=True)
