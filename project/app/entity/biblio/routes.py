from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import db4,create_app
from flask_cors import CORS,cross_origin

agent_sec = db4.collection('extension')

voie_da = db4.collection('voie')



biblio =Blueprint('biblio',__name__)

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/extension/ajouter/', methods=['POST'])
def createex():
    id=request.json['id']
    todo = agent_sec.document(id).get()
    stat1=0
    if  todo.to_dict() is None :
        agent_sec.document(id).set(request.json())
        stat1=1
    return jsonify({"stat":stat1}), 200



@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/extension/modify/', methods=['POST'])
def editex():
    id=request.json['id']
    todo = agent_sec.document(id).get()
    stat1=0
    if  todo.to_dict():
        agent_sec.document(id).update(request.json())
        stat1=1
    return jsonify({"stat":stat1}), 200


@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/voie/ajouter/', methods=['POST'])
def createvo():
    id=request.json['id']
    todo = voie_da.document(id).get()
    stat1=0
    if  todo.to_dict() is None :
        voie_da.document(id).set(request.json())
        stat1=1
    return jsonify({"stat":stat1}), 200



@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/voie/modify/', methods=['POST'])
def editvo():
    id=request.json['id']
    todo = voie_da.document(id).get()
    stat1=0
    if  todo.to_dict():
        voie_da.document(id).update(request.json())
        stat1=1
    return jsonify({"stat":stat1}), 200

