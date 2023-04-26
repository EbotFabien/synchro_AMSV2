from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import db1
import random
from flask_cors import CORS,cross_origin
import requests


agent_sec = db1.collection('Utilisateurs')




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
            if  todo.to_dict() is None :
                agent_sec.document(id).set(client)
                return jsonify({"success": True}), 200
            else:
                return jsonify({"Fail": "donnee exist deja"}), 400
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
            if  todo.to_dict() is None :
                agent_sec.document(id).set(client)
                return jsonify({"success": True}), 200
            else:
                return jsonify({"Fail": "donnee exist deja"}), 400
        
    
    

