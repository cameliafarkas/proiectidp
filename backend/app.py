from flask import Flask, render_template
from flask import request
import random
import string
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    my_string = "Professional Hair Shop"
    print("idk")
    return render_template("index.html", body=my_string)

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/products/type/<type>')
def get_products(type):
    products = []

    return render_template("products.html", products=products)

@app.route('/shopping-cart')
def shop():
    my_string = "Shopping cart"
    return render_template("shopping_cart.html", body=my_string)

@app.route('/payment')
def pay():
    my_string = "Pay"
    return render_template("payment.html", body=my_string)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
