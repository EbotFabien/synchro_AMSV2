from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import db4,create_app,db2,db3
from flask_cors import CORS,cross_origin

#db participant
agent_sec = db4.collection('Extension')

voie_da = db4.collection('voie')

#db logement
type_log = db2.collection('type_log')

extension = db2.collection('extenssion')

voie2 = db2.collection('voie')

db_piece = db2.collection('piece')

db_rubriq = db2.collection('rubriq')

db_cles = db2.collection('cles')

db_compteur = db2.collection('compteur')



biblio =Blueprint('biblio',__name__)

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/type_log/ajouter/', methods=['POST'])
def creattype_log():
    id=request.json['id']
    todo = type_log.document(id).get()
    stat1=0
    if  todo.to_dict() is None :
        type_log.document(id).set(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/piece/modify/', methods=['POST'])
def editpiece():
    id=request.json['id']
    todo = db_piece.document(id).get()
    stat1=0
    if  todo.to_dict():
        db_piece.document(id).update(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/piece/ajouter/', methods=['POST'])
def creatpiece_log():
    id=request.json['id']
    todo = db_piece.document(id).get()
    stat1=0
    if  todo.to_dict() is None :
        db_piece.document(id).set(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/compteur/ajouter/', methods=['POST'])
def creatcompteur_log():
    id=request.json['id']
    todo = db_compteur.document(id).get()
    stat1=0
    if  todo.to_dict() is None :
        db_compteur.document(id).set(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/compteur/modify/', methods=['POST'])
def editcompteur():
    id=request.json['id']
    todo = db_compteur.document(id).get()
    stat1=0
    if  todo.to_dict():
        db_compteur.document(id).update(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200


@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/rubric/modify/', methods=['POST'])
def editrubric():
    id=request.json['id']
    todo = db_rubriq.document(id).get()
    stat1=0
    if  todo.to_dict():
        db_rubriq.document(id).update(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/rubric/ajouter/', methods=['POST'])
def creatrubric_log():
    id=request.json['id']
    todo = db_rubriq.document(id).get()
    stat1=0
    if  todo.to_dict() is None :
        db_rubriq.document(id).set(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/clef/ajouter/', methods=['POST'])
def creatclef_log():
    id=request.json['id']
    todo = db_cles.document(id).get()
    stat1=0
    if  todo.to_dict() is None :
        db_cles.document(id).set(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200

@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/clef/modify/', methods=['POST'])
def editclef():
    id=request.json['id']
    todo = db_cles.document(id).get()
    stat1=0
    if  todo.to_dict():
        db_cles.document(id).update(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200


@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/type_log/modify/', methods=['POST'])
def edittype_log():
    id=request.json['id']
    todo = type_log.document(id).get()
    stat1=0
    if  todo.to_dict():
        type_log.document(id).update(request.json)
        stat1=1
    return jsonify({"stat":stat1}), 200


@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/extension/ajouter/', methods=['POST'])
def createex():
    id=request.json['id']
    todo = agent_sec.document(id).get()
    todo2 = extension.document(id).get()
    stat1=0
    stat2=0
    if  todo.to_dict() is None :
        agent_sec.document(id).set(request.json)
        stat1=1
    if  todo2.to_dict() is None :
        extension.document(id).set(request.json)
        stat2=1
    return jsonify({"stat1":stat1,"stat2":stat2}), 200



@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/extension/modify/', methods=['POST'])
def editex():
    id=request.json['id']
    todo = agent_sec.document(id).get()
    todo2 = extension.document(id).get()
    stat1=0
    stat2=0
    if  todo.to_dict():
        agent_sec.document(id).update(request.json)
        stat1=1
    if  todo2.to_dict():
        extension.document(id).set(request.json)
        stat2=1
    return jsonify({"stat1":stat1,"stat2":stat2}), 200
    


@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/voie/ajouter/', methods=['POST'])
def createvo():
    id=request.json['id']
    todo = voie_da.document(id).get()
    todo2 = voie2.document(id).get()
    stat1=0
    stat2=0
    if  todo.to_dict() is None :
        voie_da.document(id).set(request.json)
        stat1=1
    if  todo2.to_dict() is None :
        voie2.document(id).set(request.json)
        stat2=1
    return jsonify({"stat1":stat1,"stat2":stat2}), 200
    



@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@biblio.route('/voie/modify/', methods=['POST'])
def editvo():
    id=request.json['id']
    todo = voie_da.document(id).get()
    todo2 = voie2.document(id).get()
    stat1=0
    stat1=2
    if  todo.to_dict():
        voie_da.document(id).update(request.json)
        stat1=1
    if  todo2.to_dict():
        voie2.document(id).set(request.json)
        stat2=1
    return jsonify({"stat1":stat1,"stat2":stat2}), 200
   

