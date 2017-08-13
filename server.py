from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsMySecret'
app.counter = 0 #create container counter key with value 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def createPage():
    session['counter'] += 2 #here we called our counter key and increased the value by 2 
    return redirect('/')

@app.route('/reset', methods=['POST'])
def clearCounter():
    session['counter'] = 0
    return redirect('/')


app.run(debug=True)
