from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

app = Flask(__name__)

from serve import routes