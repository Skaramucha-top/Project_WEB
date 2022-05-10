from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/a1/')
def a1():
    return render_template("index.html")

@app.route('/a2/')
def a2():
    return render_template("Page_Cat-1.html")

@app.route('/a3/')
def a3():
    return render_template("Page_Doge.html")

@app.route('/a4/')
def a4():
    return render_template("Page_Parrot-1.html")

@app.route('/a5/')
def a5():
    return render_template("Page_Rabbir-1.html")


if __name__ == '__main__':
    app.run(debug=True)