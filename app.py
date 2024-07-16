from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/personal')
def personal():
    return render_template('personal.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/interests')
def interests():
    return render_template('interests.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    message = request.form['message']
    with open('comments.txt', 'a') as f:
        f.write(f'{email}: {message}\n')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
