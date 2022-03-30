from flask import Flask, render_template
from os import path


app = Flask(__name__)

if not path.isfile('templates/index.html'):
    print("HTML HAS NOT BEEN GENERATED YET.")
    print("Plase generate JSON and HTML file first.")
    exit()


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)