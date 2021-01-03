from flask import request
from . import app, jsonify
from .db import Links
import uuid


@app.route("/getAll",methods=["GET"])
def get_links():
	links = Links.get_links()
	serialized_links = [link.serializer() for link in links]
	return jsonify({"links":serialized_links}),200
@app.route("/<id>",methods=["GET"])
def get_link(id):
	link= Links.get_link()
	if link is not None:
		return jsonify({"link":link}),200
	else:
		return jsonify({"err":"no link exists"}),401	

@app.route("/save",methods =["POST"])
def save_link():
	data = request.json;
	try:
		public_id =str(uuid.uuid4())
		db_title = data["title"]
		db_link = data["link"]
		db_description = data["description"] if data["description"] else "" 

		link= Links(public_id=public_id,title=db_title,link=db_link,description=db_description)
		results=link.add_db()
	except Exception as e:
		return jsonify({"err":str(e)}),401

	return jsonify({"data":results})


@app.route("/update/<id>",methods=["POST"])
def update_link(id):
	link_data= request.json
	db_link = Links.get_link(id=id)
	try:
		db_link.access = link_data ["access"]  or db_link.access
		db_link.title = link_data["title"] or db_link.title
		db_link.description = link_data ["description"] or db_link.description
		db_link.link = link_data["link"] or db_link.link

	except Exception as e:
		return jsonify({"error":e}),401

@app.route("/delete",methods=["DELETE"])
def delete_link():
	raise NotImplementedError
