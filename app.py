from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

app.run(debug=True)