#!/usr/bin/env python
from flask import Flask, request, json
from werkzeug.routing import Rule
import time, argparse

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
		print(colors.OKBLUE+time.strftime('%Y-%m-%d %H:%M:%S')+colors.ENDC+' - ['+colors.HEADER+request.method+colors.ENDC+'] '+colors.WARNING+'/'+path+colors.ENDC+' - '+colors.FAIL+request.remote_addr+colors.ENDC)

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
	host = '127.0.0.1'
	port = 8080
	showHeaders = False
	parser = argparse.ArgumentParser(description="tool to grab and print all requests to all urls at an address.")
	parser.add_argument('-host', help='ip to bind to, default 127.0.0.1')
	parser.add_argument('-port', type=int, help='port to use, default 8080')
	parser.add_argument('-headers', action='store_true', help='show request headers')
	args = parser.parse_args()
	if args.host:
		host = args.host
	if args.port:
		port = args.port
	if args.headers:
		showHeaders = True

	print("Starting on "+host+":"+str(port))
	app.run(host=host, port=port, debug=True, use_reloader=False)
