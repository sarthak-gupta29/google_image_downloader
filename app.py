from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    keyword = request.form['keyword']
    num_images = request.form['num_images']
    email = request.form['email']
    
    # Simulate image downloading process (insert your logic here)
    
    # Send email
    try:
        send_email(email, keyword, num_images)
        return f"Downloading {num_images} images for '{keyword}' and sending to {email}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def send_email(to_email, keyword, num_images):
    from_email = os.getenv('FROM_EMAIL')  # Use environment variables
    password = os.getenv('EMAIL_PASSWORD')  # Use environment variables

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Image Downloading Completed'

    body = f"Your request for downloading {num_images} images for '{keyword}' has been completed."
    msg.attach(MIMEText(body, 'plain'))

    # SMTP Server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Changed to port 8080 for Vercel compatibility
