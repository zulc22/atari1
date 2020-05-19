from flask import Flask, redirect, render_template
import mimetypes, time, random
app = Flask(__name__)

mimetypes.add_type("text/css", ".css", True)

messages = [
    "atari0.cf ripoff",
    "scott said hi",
    "hi typicalname",
    "joe fatha",
    "Drugs ,, .,?",
    "what's 9+10",
    "IN A.D. 2020... WAR WAS BEGINNING."
]

def timestring():
    return time.strftime("%m/%d/%Y %I:%M:%S %p (%Z)")

@app.route('/')
def index():
    return render_template('index.html',
        message=random.choice(messages),
        time=timestring()
    )

if __name__ == '__main__':
    app.run()
