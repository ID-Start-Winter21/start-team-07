# PyFaceRecognition
Detect/recognize faces using face_recognition and OpenCV2

## Requirements 
### (Python packages)
- [face_recognition](https://github.com/ageitgey/face_recognition). Very cool stuff! Does the heavy lifting.
- OpenCV2, for easy webcam access. Overkill but what can you do.
- Flask. Express-like webframework.

Install packages using pip:
```
pip install opencv-python
pip install face_recognition
pip install flask
```

### Tools
- [ngrok](https://ngrok.com/). You don't need to create an account. Just download the software.


# Setup
## Start server
cd into facerecognition_server and type:

### MacOS / GNU-Linux
```
export FLASK_APP=server
flask run
```

### Windows
```
set FLASK_APP=server
flask run
```

## Make the server public via ngrok
Open a shell and:
```
ngrok http localhost:5000
```
**Beware: On a Mac, sometimes localhost doesn't work (I don't know why, yet!). The response will be a ```403 forbidden```. In this case use:***
```
ngrok http 127.0.0.1:5000
```

ngrok will create a URL that looks something like this:
```
https://ec7f-95-115-81-1.ngrok.io
```
Copy this URL and paste it into the backend
code of the Alxea skill (provided with this repo). Make sure the URL ends with a ```/```,
eg:
```python
URL = "https://ec7f-95-115-81-1.ngrok.io/"
```
Depoly it.

# Use it

You need pictures of the people you want to be recognized in `/images/<person>/<person>.png`. In the server-code you
need matching pairs of lists. One containing the name of the person, the other containing the corresponding picture of that name.
Make a GET request from Alexa to the server and get the data. You already know how to do this :)
HINT: To test the server you can also use [Postman](https://www.postman.com/) to
simulate HTTP requests!
