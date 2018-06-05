from flask import Flask, flash, session, request, redirect, render_template, url_for
from db.data_layer import get_all_bills, get_bill, create_bill, delete_bill, update_bill

app = Flask(__name__)

@app.route('/')
def index():
    b = get_all_bills()
    print('--------------------')
    print(b)
    return render_template('index.html', bills = b)

@app.route('/add_bill', methods=['POST'])
def add_bill():
    amount = request.form['amount']
    description = request.form['description']
    create_bill(amount, description)

    return redirect(url_for('index'))

app.run(debug=True)