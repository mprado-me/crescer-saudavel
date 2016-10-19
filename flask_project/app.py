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
    data = {
        "in_edit_info_mode": True,
    }
    return render_template('checkout.html', cart_table_editable=False, step=step, data=data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create-account')
def create_account():
    return render_template('create-account.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/my-account')
def my_account():
    data = {
        "in_edit_info_mode": False,
    }
    return render_template('my-account.html', data=data)

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')

@app.route('/forgot-password-email-sending')
def forgot_password_email_sending():
    return render_template('forgot-password-email-sending.html')

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