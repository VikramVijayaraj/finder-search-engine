from flask import Flask, render_template, request
from search_module import search_webpages

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def do_search():
    query = request.args.get('query', '')
    results = search_webpages(query)
    return render_template(
        "results.html",
        query=query,
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)