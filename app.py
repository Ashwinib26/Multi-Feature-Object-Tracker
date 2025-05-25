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
    ref_file = request.files.get('reference_image')
    target_file = request.files.get('target_image')

    if ref_file and target_file:
        uid = str(uuid.uuid4())[:8]

        ref_filename = f"{uid}_ref_{secure_filename(ref_file.filename)}"
        target_filename = f"{uid}_target_{secure_filename(target_file.filename)}"

        ref_path = os.path.join(UPLOAD_FOLDER, ref_filename)
        target_path = os.path.join(UPLOAD_FOLDER, target_filename)

        ref_file.save(ref_path)
        target_file.save(target_path)

        result_path, stats = process_tracking_image(ref_path, target_path, ref_filename, target_filename)

        return render_template(
            'index.html',
            original_image=url_for('static', filename=f'uploads/{target_filename}') + f"?t={int(time())}",
            processed_image=url_for('static', filename=f'results/{os.path.basename(result_path)}') + f"?t={int(time())}",
            stats=stats
        )
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
