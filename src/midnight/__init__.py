from flask import Flask, render_template
from midnight import templates
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    return app
app = create_app()

@app.route('/')
def index():
    return render_template('hello.html')