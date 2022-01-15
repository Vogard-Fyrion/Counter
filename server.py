from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html')

@app.route('/add2')
def add2():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('count')
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/amount', methods = ['POST'])
def amount():
    amount = int(request.form['amount'])
    session['count'] += amount - 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)