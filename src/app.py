#!/usr/bin/env python3

from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename

from histo import histogram


TEST_LOCAL = False # local test of the flask app VS running in a docker container
ALLOWED_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.tiff', '.bmp')
app = Flask(__name__)



@app.route('/')
def root():
    return f'Please access http://127.0.0.1:5000/histogram'


def allowed_file(filename):
    return filename.lower().endswith(ALLOWED_EXTENSIONS)


@app.route('/histogram', methods = ['POST'])
def HistograMe():
    if request.method == 'POST': # always True
        if 'image' not in request.files:
            flash('No FILES part in POST request')
            return redirect(request.url)

        f = request.files['image']
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            filepath = f'/usr/src/histograme/{filename}'
            if TEST_LOCAL:
                filepath = f'./{filename}'
            f.save(filepath)

            return histogram(filepath, False, None)

        flash("Filename not allowed")
        return redirect(request.url)



if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'super secret key' # wow much security
    # http://cdn.arstechnica.net/wp-content/uploads/2014/05/doge-hack-640x356.jpg

    app.run(debug=False, host='0.0.0.0')
