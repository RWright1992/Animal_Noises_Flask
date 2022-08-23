from application import app
from flask import Response
import random

@app.route('/', methods=['GET'])
@app.route('/get/animal', methods=['GET'])
def get_animal():
    animal = ['Dog', 'Cow', 'Cat',  'Not a cow']
    randomnum = random.randint(0,2)
    return Response(animal[randomnum], mimetype='text/plain')
