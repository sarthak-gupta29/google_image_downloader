# Image Downloader

## Description

The **Image Downloader** allows users to search and download images from Google based on a given keyword. Users can specify the number of images they want to download.

### Features:
- **Keyword Search**: Search images based on a keyword.
- **Bulk Download**: Download a specified number of images.

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Python, Flask
- **Image Downloading**: pygoogle_image
- **Deployment**: Vercel, GitHub

## Requirements

### Python 3.x
Make sure Python is installed on your system. Install the necessary dependencies using the following steps.

### Install Dependencies:
1. **Create a virtual environment** (if not already installed):
    ```bash
    pip install virtualenv
    ```

2. **Create and activate the virtual environment**:
    ```bash
    virtualenv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install project dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application Locally:
To run the application locally, use:
```bash
python app.py
