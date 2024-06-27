from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html"
    )


@app.route("/search", methods=["POST"])
def do_search():
    query = request.form["query"]
    return render_template(
        "results.html",
        query=query
    )


if __name__ == "__main__":
    app.run(debug=True)