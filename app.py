from flask import Flask, render_template, request, jsonify, send_file
import os
import zipfile
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get Pexels API Access Key from environment variables
PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    keyword = request.form['keyword']
    num_images = int(request.form['num_images'])
    headers = {
        'Authorization': PEXELS_API_KEY
    }

    # Ensure the 'downloads' directory exists
    if not os.path.exists('./downloads'):
        os.makedirs('./downloads')

    try:
        # Fetch photos from Pexels
        response = requests.get(f'https://api.pexels.com/v1/search?query={keyword}&per_page={num_images}', headers=headers)
        data = response.json()
        photos = data['photos']

        # Download each photo and save locally
        for photo in photos:
            photo_url = photo['src']['medium']  # Use 'medium' size for example
            img_response = requests.get(photo_url)
            with open(os.path.join('./downloads', f"{photo['id']}.jpg"), 'wb') as f:
                f.write(img_response.content)

        # Check if the application is running on a server
        if os.environ.get('SERVER_ENV', 'local') == 'production':
            # Create a zip file of the downloaded images
            zip_filename = './downloads/images.zip'
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for photo in photos:
                    zipf.write(os.path.join('./downloads', f"{photo['id']}.jpg"), arcname=f"{photo['id']}.jpg")

            return send_file(zip_filename, as_attachment=True)

        return jsonify({"message": f"Successfully downloaded {num_images} images for '{keyword}'."})
        
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
