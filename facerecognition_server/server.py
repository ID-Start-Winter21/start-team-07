from flask import Flask
import recognize
import json

names2encodings = None

app = Flask(__name__)

@app.before_first_request
def main():
    print('### SETUP RECOGNIZE ###')
    recognize.startCamera()
    global names2encodings # ugh, python...
    names2encodings = recognize.generateEncodings(
        ['Amir','Timo'], 

    ['./images/Amir/amir.png','./images/Timo/timo.png']
    )

@app.route('/')
def helloWorld():
    return "Hello World!"

@app.route('/face')
def face():
    # print('names2encodings')
    # print(names2encodings)
    recognizedFaces = []
    for name2encoding in names2encodings:
        if recognize.recognizeFaceForEncoding(name2encoding):
            recognizedFaces.append(name2encoding[0])

    return json.dumps(recognizedFaces)