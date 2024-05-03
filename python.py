from flask import Flask,render_template

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def funkce():
    return render_template("html.html")

if __name__ == "__main__":
    app.run()