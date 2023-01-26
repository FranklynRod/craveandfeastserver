from flask import Flask, jsonify,request, make_response, Blueprint
import firebase_admin
from firebase_admin import credentials, initialize_app, firestore

cred = credentials.Certificate("key.json")
default_app = firebase_admin.initialize_app(cred)


db = firestore.client()
user_Ref = db.collection('Account')

app = Blueprint('app', __name__)

#HELPER to Validate
#validate response is valid and exists throw error if not

#ROUTES

#Create Account

@app.route('/register',methods=["POST"])
def create_account():
    request_body = request.get_json()
    data={
        "name": request_body.name,
        "email": request_body.email
    }
    #new_account={JSON body with request body}

    return make_response(jsonify({
        'message': request_body,
    }),201) 

#Delete Account
@app.route('/account/<account_id>',methods=["DELETE"])
def delete_account(account_id):
    #validate helper function
    request_body = request.get_json()

    response_body = {
        'message': '{account_id} was deleted.'},
    return make_response(jsonify(response_body
    ),200) 

#Update account to change name or email
@app.route('/account/<account-id>',methods=["PATCH"])
def update_account():
    request_body = request.get_json()
    
    #change name=request_body["name"]
    #change email=request_body["email"]

    #current account response

    return make_response(jsonify({
        'message': request_body,
    }),200) 



#Read ALL Favorites
@app.route('/favorites',methods=["GET"])
def read_all_favorites():
    request_body = request.get_json()

    return make_response(jsonify({
        'message': request_body,
    }),200) 
    
#Delete Favorites
@app.route('/favorite/favorited/<favorited_id>',methods=["DELETE"])
def delete_favorites(favorited_id):
    #validate helper function
    request_body = request.get_json()

    response_body = {
        'message': '{favorited_id} was deleted.'},
    return make_response(jsonify(response_body
    ),200) 

