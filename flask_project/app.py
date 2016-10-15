import sys
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/product-detail')
def product_detail():
    return render_template('product-detail.html')

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