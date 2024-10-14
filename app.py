from flask import Flask, render_template, request, jsonify
from pygoogle_image import image as pi
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    keyword = request.form['keyword']
    num_images = request.form['num_images']
    
    try:
        # Download images using pygoogle_image
        pi.download(keyword, limit=int(num_images))
        return jsonify({"message": f"Successfully downloaded {num_images} images for '{keyword}'."})
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
