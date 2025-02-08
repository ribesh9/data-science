from flask import Flask

print("Hello I am inside file")

def welcom():
    print("Hello inside welcome")

def Thankyou():
    print("Hello inside Thank you")
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Home"

@app.route('/login')

def login():
    return "Welcome to login"

if __name__=='__main__':
    app.run(debug=True)
    #app.run('127.0.0.1 this is ','3232 this is port',debug=True)