from flask import Flask, Response, redirect, render_template, request
import mimetypes, time, random
app = Flask(__name__)

mimetypes.add_type("text/css", ".css", True)

messages = [
    "atari0.cf ripoff",
    "scott said hi",
    "hi typicalname",
    "*heavy breathing* ...Hi Kevin...",
    "joe fatha",
    "Drugs ,, .,?",
    "what's 9+10",
    "IN A.D. 2020... WAR WAS BEGINNING."
]

def timestring():
    return time.strftime("%m/%d/%Y %I:%M:%S %p (%Z)")

def generate_header(pagename):
    return render_template('header.html',
        message=random.choice(messages),
        time=timestring(),
        pagename=pagename
    )

@app.route('/')
def index():
    pagename = "⌂ index"

    return render_template('index.html',
        headerhtml=generate_header(pagename)
    )

@app.route('/login')
def loginform():
    pagename = "※ login"

    return render_template('loginform.html',
        headerhtml=generate_header(pagename)
    )

@app.route('/signup')
def signupform():
    pagename = "✆ sign up"

    return render_template('signupform.html',
        headerhtml=generate_header(pagename)
    )

@app.route('/api/restart')
def restart_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

    response = Response(
        "Restarting server...<br>Page will redirect to index in a few seconds."
    )
    response.headers['refresh'] = '3;url=/'
    return response

if __name__ == '__main__':
    app.run()
