from . import app, jsonify


@app.route("/")
def runs():
    return jsonify({"hello": "links"})
