#!/usr/bin/env python

import sys
import string

#sys.path.append('..')
from flask import Flask, render_template, url_for, request, redirect, session, g, Blueprint
from werkzeug import secure_filename
from config import flask_secret_key

import process	# business logic happens here

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['csv', 'json', 'rss', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
angularBlueprint = Blueprint('app', __name__, static_folder='/app/')
print angularBlueprint.__dict__
app.register_blueprint(angularBlueprint, url_prefix='/app')

app.debug = True
if app.debug:
	import pdb
app.secret_key = flask_secret_key


# ============== REGULAR REQUESTS  ==============

@app.route("/")
def index():
	#return render_template('index.html')
	return redirect( url_for('static', filename='index.html'))
	"""
	filename = url_for('app.static', filename='index.html')
	print "FILENAME:", filename
	return "does not work... :("
	"""


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'GET':
		return "hello"
	if request.method == 'POST':
		csvfilenames = ['communityFile', 'memberFile', 'servicesFile' ]
		for filename in csvfilenames:
			file = request.files[filename]
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				return redirect(url_for('uploaded_file',
										filename=filename))
	return "ERROR"

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
