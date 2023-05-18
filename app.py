from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')    
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
