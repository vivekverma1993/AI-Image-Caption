from flask import Blueprint, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from .services.image_captioning import generate_caption
from .services.object_detection import detect_objects

main_bp = Blueprint('main', __name__)
UPLOAD_FOLDER = 'static/uploads/'

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    image = request.files['image']
    filename = secure_filename(image.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    image.save(filepath)

    caption = generate_caption(filepath)
    objects = detect_objects(filepath)

    return jsonify({"caption": caption, "objects": objects})
