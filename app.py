import flask
# to install go to View - Tool Windows - Terminal
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/products')
def products():
    return 'This will be our product page'


@app.route('/contacts')
def contacts():
    return 'This is our contacts page'


@app.route('/order')
def order():
    return 'Make an order'

# check if the __name__  is the main project
if __name__ == '__main__':
    app.debug = True
    app.run()


    #http://127.0.0.1:5000/home
    #http://127.0.0.1:5000/products





