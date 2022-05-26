from crypt import methods
import json
from webbrowser import get
from flask import Flask,jsonify,request 
app = Flask(__name__)
contact = [
    {
        'id':1,
        'contact':'928319212',
        'name':'Raju',
       
    },{
        'id':2,
        'contact':'928319212',
        'name':'Rahul',
      
    },
]
@app.route('/add-data',methods=["POST"])
def add_task ():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)

    task = {
        'id':contact[-1]['id']+1,
        'contact': request.json['contact'],
        'name': request.json.get('name',""),
       
        }
    contact.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })
@app.route("/get-data")
def get_task ():
    return jsonify({
        "data":contact,
        
    })
if(__name__ == "__main__"):
    app.run(debug = True)