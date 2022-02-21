from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'Contact': '9987644456',
        'Name': 'Raju',
        'done': False
    },
    {
        'id': 2,
        'Contact': '987643222',
        'Name': 'Rahul',
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "hello_world"

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        }, 400)
    
    task  = {
        'id': tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Conatcat': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message":"Task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks

    })
if(__name__ ==  "__main__"):
    app.run(debug = True)