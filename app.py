from flask import Flask, render_template

# hi tushar
app=Flask(__name__)

@app.route("/")
def home():
    return render_template(index.html)