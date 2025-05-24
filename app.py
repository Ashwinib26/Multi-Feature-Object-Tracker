from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import uuid
from time import time
from utils.tracker import process_tracking_image

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', original_image=None, processed_image=None)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('image')
    threshold = float(request.form.get('threshold', 0.1))  # example slider for corner threshold

    if file:
        unique_id = str(uuid.uuid4())[:8]
        filename = f"{unique_id}_{secure_filename(file.filename)}"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        result_path, stats = process_tracking_image(filepath, filename, threshold)

        return render_template(
            'index.html',
            original_image=url_for('static', filename=f'uploads/{filename}') + f"?t={int(time())}",
            processed_image=url_for('static', filename=f'results/{os.path.basename(result_path)}') + f"?t={int(time())}",
            stats=stats
        )
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
