from flask import Flask, render_template, request, jsonify, send_file
import os
from dotenv import load_dotenv
import requests
import zipfile
import io

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

    # Determine if we're running locally or on a server
    is_local = os.getenv('FLASK_ENV') == 'development'

    try:
        # Fetch photos from Pexels
        response = requests.get(f'https://api.pexels.com/v1/search?query={keyword}&per_page={num_images}', headers=headers)
        data = response.json()
        photos = data['photos']

        if is_local:
            # Ensure the 'downloads' directory exists
            if not os.path.exists('./downloads'):
                os.makedirs('./downloads')

            # Download each photo locally
            for photo in photos:
                photo_url = photo['src']['medium']  # Use 'medium' size for example
                img_response = requests.get(photo_url)
                with open(os.path.join('./downloads', f"{photo['id']}.jpg"), 'wb') as f:
                    f.write(img_response.content)

            return jsonify({"message": f"Successfully downloaded {num_images} images for '{keyword}'."})
        else:
            # Create a zip file in memory
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                for photo in photos:
                    photo_url = photo['src']['medium']
                    img_response = requests.get(photo_url)
                    zip_file.writestr(f"{photo['id']}.jpg", img_response.content)

            zip_buffer.seek(0)

            # Send the zip file for download
            return send_file(
                zip_buffer,
                mimetype='application/zip',
                as_attachment=True,
                download_name=f"{keyword}_images.zip"
            )

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)