from Flask import flask, render_template


app=Flask(__name__)

@app.route("/")
def home():
    return render_template(index.html)