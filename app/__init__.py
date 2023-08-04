from flask import Flask, render_template
from config import Config
from .auth.routes import auth
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


app.register_blueprint(auth)

app.config.from_object(Config)

imageFolder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = imageFolder

@app.route("/")
def index():
    image1 = os.path.join(app.config['UPLOAD_FOLDER'], 'businessman.png')
    imageList = os.listdir('static/pics')
    imageList = ['pics/' + image for image in imageList]
    return render_template("index.html", imageList=imageList)


