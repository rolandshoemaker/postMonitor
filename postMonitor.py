#!/usr/bin/env python
from flask import Flask, request, json
from werkzeug.routing import Rule
import time

import pprint

app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app.url_map.add(Rule('/', endpoint='index'))
app.url_map.add(Rule('/<path:path>', endpoint='other'))

@app.endpoint('index')
@app.endpoint('other')
def catch_all(path=None):
	if path == "" or path == None:
		print(time.strftime('%Y-%m-%d %H:%M:%S')+' - ['+request.method+'] / - '+request.remote_addr)
	else:
		print(time.strftime('%Y-%m-%d %H:%M:%S')+' - ['+request.method+'] /'+path+' - '+request.remote_addr)

	if showHeaders == True:
		for i in request.headers:
			print("\t\t"+i[0]+": "+i[1])

	if request.args:
		print("\t[URL Variables]")
		#pprint.pprint(request.args)
		for i in request.args:
			print("\t\t"+i+": "+request.args[i])

	if request.headers['Content-Type'].split(';')[0] == "application/json" and request.json:
		print("\t[JSON]")
		print(json.dumps(request.json, indent=2, sort_keys=False, separators=(',', ': ')))

	if request.headers['Content-Type'].split(';')[0] == "multipart/form-data" and request.form:
		print("\t[Multipart form-data]")
		#pprint.pprint(request.form)
		for i in request.form:
			print("\t\t"+i+": "+request.form[i])

	if request.headers['Content-Type'].split(';')[0] == "application/x-www-form-urlencoded" and request.form:
		print("\t[URL Encoded form-data]")
		#pprint.pprint(request.form) 
		for i in request.form:
			print("\t\t"+i+": "+request.form[i])

	return "^__^"

if __name__ == "__main__":
	host = "192.168.1.130"
	port = 8080
	showHeaders = True
	app.run(host=host, port=port, debug=True)
