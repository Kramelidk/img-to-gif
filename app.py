from flask import Flask, request, render_template, send_file
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file uploaded', 400

    image_file = request.files['image']

    if image_file.filename == '':
        return 'No selected file', 400

    # Perform the image to GIF conversion
    img = Image.open(image_file)
    gif_path = 'output.gif'  # Relative to the current working directory
    img.save(gif_path, 'GIF')

    # Send the GIF file with the appropriate content type
    return send_file(gif_path, as_attachment=True, mimetype='image/gif')

if __name__ == '__main__':
    app.run()
