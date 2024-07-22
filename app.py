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

@app.route('/tech/html_css')
def tech_html_css():
    return render_template('tech_html_css.html')

@app.route('/tech/react')
def tech_react():
    return render_template('tech_react.html')

@app.route('/tech/javascript')
def tech_javascript():
    return render_template('tech_javascript.html')

@app.route('/interests')
def interests():
    return render_template('interests.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    with open('comments.txt', 'a') as f:
        f.write(f'{name}, {email}: {message}\n')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
