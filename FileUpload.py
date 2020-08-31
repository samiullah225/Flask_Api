from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__,template_folder='./')


@app.route('/')
def upload_file_front():
    return render_template('UploadFile.html')


@app.route('/upload', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)