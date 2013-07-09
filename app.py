import os
from flask import Flask, Response, json

app = Flask(__name__)

@app.route("/")
def home():
  data = ['Prinsengracht', 'Keizersgracht', 'Herengracht', 'Lauriergracht']
  resp = Response(json.dumps(data), status=200, mimetype='application/json')
  return resp

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
