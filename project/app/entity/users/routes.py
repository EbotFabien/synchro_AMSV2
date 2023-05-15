from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import db1,db2
import random
from flask_cors import CORS,cross_origin
import requests


agent_sec = db1.collection('Utilisateurs')
log_user = db2.collection('user')




users =Blueprint('users',__name__)


@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@users.route('/util/ajouter/<typo>', methods=['POST'])
def createu(typo):
    if typo == "all":
        if request:
            id=str(request.json[0]['id'])
            client={
                "compte_client":request.json[0]['compte_client'],
                "email":request.json[0]['user']['email'],
                "nom": request.json[0]['user']['nom'],
                "pass": request.json[0]['mdp'],
                "prenom": request.json[0]['user']['prenom'],
                "role": request.json[0]['user']['group'],
                "telephone": request.json[0]['telephone'],
                "id": str(request.json[0]['id'])
            }
            todo = agent_sec.document(id).get()
            todo1=log_user.document(id).get()
            stat1=0
            stat2=0
            if  todo.to_dict() is None :
                agent_sec.document(id).set(client)
                stat1=1
            if  todo1.to_dict() is None :
                log_user.document(id).set(client)
                stat2=1
            return jsonify({"stat":stat1,"stat2":stat2}), 200
            
    else:
        if request:
            id=str(request.json[0]['id'])
            client={
                "email":request.json[0]['user']['email'],
                "nom": request.json[0]['user']['nom'],
                "pass": request.json[0]['mdp'],
                "prenom": request.json[0]['user']['prenom'],
                "role": request.json[0]['user']['group'],
                "telephone": request.json[0]['telephone'],
                "id": str(request.json[0]['id'])
            }
            todo = agent_sec.document(id).get()
            todo1=log_user.document(id).get()
            stat1=0
            stat2=0
            if  todo.to_dict() is None :
                agent_sec.document(id).set(client)
                stat1=1
            if  todo1.to_dict() is None :
                log_user.document(id).set(client)
                stat2=1
            return jsonify({"stat":stat1,"stat2":stat2}), 200
        


@cross_origin(origin=["http://127.0.0.1:5274","http://195.15.228.250","*"],headers=['Content-Type','Authorization'],automatic_options=False)
@users.route('/util/edit/', methods=['POST'])
def editu():
    if request:
        if request.json[0]['user']['group'] == "Administrateur":
            id=str(request.json[0]['id'])
            client={
                "email":request.json[0]['user']['email'],
                "nom": request.json[0]['user']['nom'],
                "pass": request.json[0]['mdp'],
                "prenom": request.json[0]['user']['prenom'],
                "role": request.json[0]['user']['group'],
                "telephone": request.json[0]['telephone'],
                "id": str(request.json[0]['id'])
            }
            todo = agent_sec.document(id).get()
            todo1 =log_user.document(id).get()
            stat1=0
            stat2=0
            if  todo.to_dict():
                agent_sec.document(id).update(client)
                stat1=1
            if  todo1.to_dict():
                log_user.document(id).update(client)
                stat2=1
            return jsonify({"stat":stat1,"stat2":stat2}), 200
        

        else:
            if request:
                id=str(request.json[0]['id'])
                client={
                    "compte_client":request.json[0]['compte_client'],
                    "email":request.json[0]['user']['email'],
                    "nom": request.json[0]['user']['nom'],
                    "pass": request.json[0]['mdp'],
                    "prenom": request.json[0]['user']['prenom'],
                    "role": request.json[0]['user']['group'],
                    "telephone": request.json[0]['telephone'],
                    "id": str(request.json[0]['id'])
                }
                todo = agent_sec.document(id).get()
                todo1 =log_user.document(id).get()
                stat1=0
                stat2=0
                if  todo.to_dict():
                    agent_sec.document(id).update(client)
                    stat1=1
                if  todo1.to_dict():
                    log_user.document(id).update(client)
                    stat2=1
                return jsonify({"stat":stat1,"stat2":stat2}), 200



    

