import sys
from flask import Flask, jsonify, render_template, request

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

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog-post')
def blog_post():
    return render_template('blog-post.html')

@app.route('/shopping-cart')
def shopping_cart():
    return render_template('shopping-cart.html', cart_table_editable=True)

@app.route('/checkout')
def checkout():
    step = request.args.get('step')
    step = int(step)
    return render_template('checkout.html', cart_table_editable=False, step=step)

@app.route('/login')
def login():
    return render_template('login.html')

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