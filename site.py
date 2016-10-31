from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Frontpage.html")

@app.route('/biz')
def biz():
    return render_template("donate.html")

@app.route('/donate')
def donate():
    return render_template("Patronize.html")


if __name__ == "__main__":
    app.run()
