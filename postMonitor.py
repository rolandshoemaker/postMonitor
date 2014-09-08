#!/usr/bin/env python
from flask import Flask, request, json
from werkzeug.routing import Rule
import time

import pprint

app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

app.url_map.add(Rule('/', endpoint='index'))
app.url_map.add(Rule('/<path:path>', endpoint='other'))

@app.endpoint('index')
@app.endpoint('other')
def catch_all(path=None):
	if path == "" or path == None:
		print(colors.OKBLUE+time.strftime('%Y-%m-%d %H:%M:%S')+colors.ENDC+' - ['+colors.HEADER+request.method+colors.ENDC+'] '+colors.WARNING+'/'+colors.ENDC+' - '+colors.FAIL+request.remote_addr+colors.ENDC)
	else:
		print(colors.OKBLUE+time.strftime('%Y-%m-%d %H:%M:%S')+colors.ENDC+' - ['+colors.HEADER+request.method+colors.ENDC+'] /'+colors.WARNING+path+colors.ENDC+' - '+colors.FAIL+request.remote_addr+colors.ENDC)

	if showHeaders == True:
		print("\t["+colors.OKGREEN+"Header"+colors.ENDC+"]")
		for i in request.headers:
			print("\t\t"+i[0]+": "+i[1])

	if request.args:
		print("\t["+colors.OKGREEN+"URL Variables"+colors.ENDC+"]")
		for i in request.args:
			print("\t\t"+i+": "+request.args[i])

	if request.headers['Content-Type'].split(';')[0] == "multipart/form-data" and request.form:
		print("\t["+colors.OKGREEN+"Multipart form-data"+colors.ENDC+"]")
		for i in request.form:
			print("\t\t"+i+": "+request.form[i])

	if request.headers['Content-Type'].split(';')[0] == "application/x-www-form-urlencoded" and request.form:
		print("\t["+colors.OKGREEN+"URL Encoded form-data"+colors.ENDC+"]")
		for i in request.form:
			print("\t\t"+i+": "+request.form[i])

	if request.headers['Content-Type'].split(';')[0] == "application/json" and request.json:
		print("\t["+colors.OKGREEN+"JSON"+colors.ENDC+"]")
		for i in json.dumps(request.json, indent=2, sort_keys=False, separators=(',', ': ')).split("\n"):
			print("\t\t"+i)

	if request.headers['Content-Type'].split(';')[0] == "text/plain":
		print("\t["+colors.OKGREEN+"Plain text"+colors.ENDC+"]")
		for i in request.data.split("\n"):
			print("\t\t"+i)

	return "^__^\n"

if __name__ == "__main__":
	host = "192.168.1.130"
	port = 8080
	showHeaders = True
	app.run(host=host, port=port, debug=True)
