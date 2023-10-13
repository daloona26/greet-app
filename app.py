from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "helloworld"

@app.route("/")
@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route('/greet', methods=["POST", "GET"])
def greet():
    input = request.form.get('name_input')
    flash(f"Hi {input}, great to see you")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)