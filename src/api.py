from PeNumbers import PeNumbers
import flask

from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/pe', methods=['GET'])
def pe():
  query_parameters = request.args
  number = query_parameters.get('number')
  p = PeNumbers.PeNumbers()

  try:
    return p.getResult(int(number)), 200
  except:
    return {}, 400

if __name__ == "__main__":
    app.run(host= '0.0.0.0')

