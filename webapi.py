#!/usr/bin/env python

import sys
import string

#sys.path.append('..')
from flask import Flask, render_template, url_for, request, redirect, session, g
from werkzeug import secure_filename
from config.py import flask_secret_key

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['csv', 'json', 'rss', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.debug = True
if app.debug:
	import pdb
app.secret_key = flask_secret_key


# ============== REGULAR REQUESTS  ==============

@app.route("/")
def index():
	return "hello"


@app.route('/upload.py', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'GET':
		return "hello"
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return "uploaded"

def dbgFlask(msg=None):
	dbgInfo('session', session)
	dbgInfo('request', request)
	dbgInfo('app', app)
	dbgInfo('request args', request.values)
	dbgInfo('request cookies', request.cookies)
	if msg: dbgInfo('CUSTOM MSG', msg.upper())
	#if flask.g: dbgInfo('g', flask.g)
	#if get_flashed_message(): dbgInfo('flashed messages', get_flashed_messages())
	#if current_app: dbgInfo('current_app', current_app)


# ============== HELPERS  ==============
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def main():
	app.run()
	return 0

if __name__ == "__main__":
    sys.exit(main())
