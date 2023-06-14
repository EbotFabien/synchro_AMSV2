from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import db3
from flask_cors import CORS,cross_origin

db_edl = db3.collection('logement')




edl=Blueprint('edl',__name__)

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@edl.route('/edl/logement/ajouter/', methods=['POST'])
def createp():
    id=request.json['id_']
    todo = db_edl.document(id).get()
    stat1=0
    if  todo.to_dict() is None :
        db_edl.document(id).set(request.json())
        stat1=1
    return jsonify({"stat":stat1}), 200

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@edl.route('/edl/logement/edit/', methods=['POST'])
def editp():
    id=request.json['_id']
    todo = edl.document(id).get()
    stat1=0
    if  todo.to_dict():
        edl.document(id).update(request.json())
        stat1=1
    return jsonify({"stat":stat1}), 200
