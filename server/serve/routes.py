from flask import  render_template
from flask_socketio import emit, send
from serve import app, socketio

@app.route('/')
def home():
    return render_template('home.html')

@socketio.on("message")
def sendMessage(message):
    print(message)
    send(message, broadcast=True)

@app.route('/chat')
def chat():
    return render_template('chat.html')

#----------------------------------Error handle ---------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages-error-404.html'), 404