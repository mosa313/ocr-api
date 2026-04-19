from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import base64
import io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    data = request.json['image'].split(',')[1]
    img = Image.open(io.BytesIO(base64.b64decode(data)))

    text = pytesseract.image_to_string(img)

    return jsonify({"text": text})

@app.route('/')
def home():
    return "OCR API Running"

if __name__ == '__main__':
    app.run()
