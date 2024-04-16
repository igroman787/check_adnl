import os
import json
import base64
from flask import Flask, render_template, request, send_from_directory
from werkzeug.exceptions import HTTPException
from mytonlib.adnl import AdnlUdpClient


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon")
#end define

@app.route('/')
def index():
	return render_template("index.html")
#end define

@app.route("/adnl_check", methods=["POST"])
def adnl_check():
	host = request.form.get("host") or request.json.get("host")
	port = request.form.get("port") or request.json.get("port")
	pubkey = request.form.get("pubkey") or request.json.get("pubkey")
	try: 
		adnl = AdnlUdpClient()
		adnl.connect(host, int(port), pubkey)
		result = {'ok': True, 'message': ''}
	except Exception as ex:
		message = f'host: {host}, port: {port}, pubkey: {pubkey}, error: {ex}'
		result = {'ok': False, 'message': message}
	return json.dumps(result, indent=4)
#end define

@app.errorhandler(HTTPException)
def handle_exception(error):
	title_text = f"{error.code} {error.name}"
	return render_template("error_page.html", title_text=title_text, error_code=error.code, error_name=error.name, error_description=error.description), error.code
#end define

if __name__ == "__main__":
	app.logger.info("start web server")
	app.run(host="127.0.0.1", port=8000)
#end define
