from flask import Flask, jsonify,request, make_response, Blueprint
import firebase_admin
from firebase_admin import credentials, initialize_app, firestore

cred = credentials.Certificate("key.json")
default_app = firebase_admin.initialize_app(cred)


db = firestore.client()
# user_Ref = db.collection('Account')

app = Flask(__name__)

#HELPER to Validate
#validate response is valid and exists throw error if not

#ROUTES

#Create Account
@app.route('/register',methods=["POST"])
def create_account():
    request_body = request.get_json()
    data={
        "name": request_body["name"],
        "email": request_body["email"]
    }
    db.collection('Account').add(data)

    return make_response(jsonify({
        'message': request_body,
    }),201) 

#Delete Account
@app.route('/account/<account_id>',methods=["DELETE"])
def delete_account(account_id):
    try:
        db.collection('Account').document(account_id).delete()
        response_body = {
        'message': f'Account {account_id} was deleted.'}
        return make_response(jsonify(response_body
        ),200)
    except Exception as e:
        return f"An Error Occured: {e}"


# # Update account to change name or email
@app.route('/account/<account_id>',methods=["PUT"])
def update_account(account_id):
    try:
        db.collection('Account').document(account_id).update(request.json)
        return jsonify({'message': f'Account{account_id} was updated.'}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

#Read ALL Favorites
@app.route('/account/<account_id>/favorites',methods=["GET"])
def read_all_favorites(account_id):
    # docs= db.collection('Favorites').stream()
    docs = db.collection('Account').document(account_id).collection('Favorites').stream()
    # doc_list=[f'{doc.id} => {doc.to_dict()}' for doc in docs]
    doc_list=[]
    for doc in docs:
        doc_list.append(f'{doc.id} => {doc.to_dict()}')
    return (jsonify(doc_list),200)
            # return make_response(jsonify(f'{doc.id} => {doc.to_dict()}'),200) 
        
# #Delete One Favorite
@app.route('/account/<account_id>/favorites/<favorites_id>',methods=["DELETE"])
def delete_one_favorite(account_id,favorites_id):
    try:
        # favorites_num = request.args.get('favorites_id')
        db.collection('Account').document(account_id).collection('Favorites').document(favorites_id).delete()
    # db.collection(‘Accounts’).document(account_id).collection(‘Favorites’).document(favorites_id)
        # db.collection('Favorites').document(favorites_id).delete()
        response_body = {
        'message': f'Favorites #{favorites_id} was deleted.'}
        return make_response(jsonify(response_body
        ),200)
    except Exception as e:
        return f"An Error Occured: {e}"


# #Get specific Reciepe
# def get_one_reciepe():


if __name__ == '__main__':
    app.run(debug=True)