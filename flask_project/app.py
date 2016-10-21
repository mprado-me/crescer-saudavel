import sys
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/sobre-nos')
def about_us():
    return render_template('about-us.html')

@app.route('/produtos')
def products():
    return render_template('products.html')

@app.route('/produto')
def product_detail():
    return render_template('product-detail.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/post')
def blog_post():
    return render_template('blog-post.html')

@app.route('/carrinho')
def shopping_cart():
    return render_template('shopping-cart.html', cart_table_editable=True)

@app.route('/finalizacao-de-compra')
def checkout():
    step = request.args.get('step')
    if not step:
        step = "1"
    step = int(step)
    data = {
        "in_edit_info_mode": True,
    }
    return render_template('checkout.html', cart_table_editable=False, step=step, data=data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/criar-conta')
def create_account():
    return render_template('create-account.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/minha-conta')
def my_account():
    data = {
        "in_edit_info_mode": False,
    }
    return render_template('my-account.html', data=data)

@app.route('/recuperaçao-de-senha')
def forgot_password():
    return render_template('forgot-password.html')

@app.route('/envio-do-email-de-recuperacao-de-senha')
def forgot_password_email_sending():
    return render_template('forgot-password-email-sending.html')

@app.route('/nova-senha')
def new_password():
    return render_template('new-password.html')

@app.route('/pedido')
def order():
    return render_template('order.html')

if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1] == 'local':
		app.debug = True
		app.run(host='0.0.0.0', port=5000)
	else:
		app.run()