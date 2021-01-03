from . import app, jsonify

@app.route("/<id>",methods=["GET"])
def get_link(id):
	# make call  to  the datab
	raise NotImplementedError

@app.route("/save",methods =["POST"])
def save_link():
	raise NotImplementedError


@app.route("/update",methods=["POST"])
def update_link():
	raise NotImplementedError

@app.route("/delete",methods=["DELETE"])
def delete_link():
	raise NotImplementedError
