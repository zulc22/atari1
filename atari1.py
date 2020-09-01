from flask import Flask, Response, redirect, render_template, request
import mimetypes, time, random
app = Flask(__name__)

mimetypes.add_type("text/css", ".css", True)

messages = [
    "🦀 atari0.cf is dead and this is all that's left 🦀",
    "scott said hi",
    "scott said die",
    "*heavy breathing* ...Hi Kevin...",
    "joe fatha",
    "hey lois",
    "Drugs ,, .,?",
    "what's 9+10",
    "IN A.D. 2020... WAR WAS BEGINNING.",
    "HAH! GAEEEEY 🏳‍🌈🏳‍🌈🏳‍🌈",
    "we don't actually know japanese 😳",
    "super mario in real life exposed (GONE SEXUAL)",
    "sans undertale said trans rights",
    "whose typicalname?",
    "アタリツー! ♥"
]

def is_production():
    """ Determines if app is running on the production server or not.
    Get Current URI.
    Extract root location.
    Compare root location against developer server value 127.0.0.1:5000.
    :return: (bool) True if code is running on the production server, and False otherwise.
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url != developer_url

def timestring():
    return time.strftime("%m/%d/%Y %I:%M:%S %p (%Z)")

def generate_header(pagename):
    return render_template('header.html',
        message=random.choice(messages),
        time=timestring(),
        pagename=pagename,
        production=is_production()
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
    if is_production():
        return Response("Running on a production server! Server will not restart.", status=400)

    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

    return Response(
        "Restarting server...<br>Page should redirect to <a href='/'>index</a> in a few seconds.",
        headers={
            "refresh": "3;url=/"
        }
    )

@app.route('/api/signup', methods=['POST'])
def signup():
    # TODO
    return Response(
        "Signup not implemented.",
        status=400
    )

if __name__ == '__main__':
    app.run()
