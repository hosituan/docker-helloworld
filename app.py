import random
import string
import os
import pytesseract
from PIL import Image
from flask import Flask,flash,request,redirect,url_for,send_from_directory,send_file,jsonify, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"


def generate_random_string(length):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits
    
    # Generate a random string by choosing a random character from the set
    random_string = ''.join(random.choice(characters) for i in range(length))
    
    return random_string

@app.route('/mst/captcha', methods=['POST'])
def extractCaptcha():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    file_name = generate_random_string(5) + ".jpg"
    file_path = os.path.join(os.getcwd(), file_name)
    file.save(file_path)
    img = Image.open(file_path)
    custom_config = r'--oem 3 --psm 6'
    string = pytesseract.image_to_string(img, config=custom_config)
    os.remove(file_path)
    return string.replace(" ", "")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
