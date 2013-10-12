#!/usr/bin/env python

import sys
import string

#sys.path.append('..')
from flask import Flask, render_template, url_for, request, redirect, session, g
app = Flask(__name__)
from config.py import flask_secret_key

app.debug = True
if app.debug:
	import pdb
app.secret_key = flask_secret_key


# ============== REGULAR REQUESTS  ==============

@app.route("/")
def index():
	return "hello"

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

def main():
	app.run()
	return 0

if __name__ == "__main__":
    sys.exit(main())
