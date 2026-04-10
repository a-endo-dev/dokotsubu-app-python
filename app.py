from flask import Flask, render_template, request

app = Flask(__name__)

mutter_list = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("name")
    password = request.form.get("password")

    if password == "1234":
        return render_template("main.html", name=name, mutter_list=mutter_list)
    else:
        return "ログイン失敗"

@app.route("/post", methods=["POST"])
def post():
    name = request.form.get("name")
    text = request.form.get("text")

    if text:
        mutter = name + "： " + text
        mutter_list.insert(0, mutter)

    return render_template("main.html", name=name, mutter_list=mutter_list)

if __name__ == "__main__":
    app.run(debug=True)