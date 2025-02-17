# app.py
from flask import Flask, jsonify, request
import requests, certifi

app = Flask(__name__)

# API Route: /api/random_joke (hämtar en rolig gåta från ett externt API)
@app.route('/api/random_joke', methods=['GET'])
def random_joke():
    # Anropar ett externt API för att hämta en slumpmässig skämt
    response = requests.get('https://v2.jokeapi.dev/joke/Programming?type=twopart', verify=certifi.where())
    joke = response.json()

    return jsonify(setup=joke['setup'], punchline=joke['delivery'])

if __name__ == '__main__':
    app.run(debug=True)
