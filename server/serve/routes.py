from flask import  render_template
from serve import app


@app.route('/')
def home():
    return render_template('chat.html')
