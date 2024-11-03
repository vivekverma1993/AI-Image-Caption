import os

def ensure_upload_folder_exists():
    if not os.path.exists('static/uploads'):
        os.makedirs('static/uploads')
