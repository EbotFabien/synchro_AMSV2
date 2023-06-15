from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import db1,db2,db3
from flask_cors import CORS,cross_origin

db_participant = db3.collection('participant')

client_users = db1.collection('Agentsec')

client_logement = db2.collection('client')

client_edl = db3.collection('client')




participants =Blueprint('part',__name__)

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@participants.route('/client/ajouter/', methods=['POST'])
def createclient():
    id=request.json['id']
    todo = client_users.document(id).get()
    todo2 = client_logement.document(id).get()
    todo3 = client_edl.document(id).get()
    stat1=0
    stat2=0
    stat3=0
    if  todo.to_dict() is None :
        client_users.document(id).set(request.json)
        stat1=1
    if  todo2.to_dict() is None :
        client_logement.document(id).set(request.json)
        stat2=1
    if  todo3.to_dict() is None :
        client_edl.document(id).set(request.json)
        stat3=1
    return jsonify({"stat":stat1,"stat2":stat2,"stat3":stat3}), 200

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@participants.route('/client/edit/', methods=['POST'])
def editclient():
    id=request.json['id']
    todo = client_users.document(id).get()
    todo2 = client_logement.document(id).get()
    todo3 = client_edl.document(id).get()
    stat1=0
    stat2=0
    stat3=0
    if  todo.to_dict():
        client_users.document(id).update(request.json)
        stat1=1
    if  todo2.to_dict():
        client_logement.document(id).update(request.json)
        stat2=1
    if  todo3.to_dict():
        client_edl.document(id).update(request.json)
        stat3=1    
    return jsonify({"stat":stat1,"stat2":stat2,"stat3":stat3}), 200


@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@participants.route('/parti/ajouter/', methods=['POST'])
def createp():
    id=request.json['id']
    todo = db_participant.document(id).get()
    stat1=0
    if  todo.to_dict() is None :
        db_participant.document(id).set(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200


@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@participants.route('/parti/edit/', methods=['POST'])
def editp():
    id=request.json['id']
    todo = db_participant.document(id).get()
    stat1=0
    if  todo.to_dict():
        db_participant.document(id).update(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200
