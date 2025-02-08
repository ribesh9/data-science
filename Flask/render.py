from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')


def hello(name=None):
    return render_template('hello.html')

@app.route('/hello/loginpage',method = ['POST'])
def loginpage():
    return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    

if __name__=='__main__':
    app.run(debug=True)