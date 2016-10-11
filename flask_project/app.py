import sys
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running!'


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1] == 'local':
		app.debug = True
		app.run(host='0.0.0.0', port=5000)
	else:
		app.run()