from flask import Flask, jsonify, request
import requests, certifi
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(app, doc='/swagger', prefix='/api')
ns = api.namespace('jokes', description='Fetch funny programming jokes')
api.add_namespace(ns)
joke_model = api.model('Joke', {
    'setup': fields.String(description='Question or setup of joke', required=True),
    'punchline': fields.String(description='Punchline or end of joke', required=True)
})


# Definiera en resurs för att hämta ett skämt
@ns.route('/random')
class Joke(Resource):
    @api.marshal_with(joke_model)
    def get(self):
        """
        Return a random joke.
        """
        response = requests.get('https://v2.jokeapi.dev/joke/Programming?type=twopart', verify=certifi.where())
        joke = response.json()
        return {
            "setup": joke['setup'],
            "punchline": joke['delivery']
        }

if __name__ == '__main__':
    app.run(debug=True)
