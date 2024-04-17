from waitress import serve
from web import app

serve(app, host='0.0.0.0', port=8080)
