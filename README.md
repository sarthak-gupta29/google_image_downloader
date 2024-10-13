# Image Downloader

## Description

This **Image Downloader** allows users to download images from Google based on a search keyword. Users can specify the number of images to download and provide an email address to receive a confirmation once the request is processed.

### Features:
- **Keyword Search**: Enter a keyword to search images.
- **Bulk Download**: Specify the number of images.
- **Email Notification**: Receive a confirmation email after the process.

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Python, Flask
- **Email**: Gmail SMTP
- **Deployment**: Heroku, GitHub

## Requirements

### Python 3.x
To run this project, make sure Python is installed on your system. You also need the following dependencies.

### Install Dependencies:
Create a virtual environment and install the dependencies by running the following:

```bash
# Install virtual environment (if not installed)
pip install virtualenv

# Create and activate a virtual environment
virtualenv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install project dependencies
pip install -r requirements.txt
