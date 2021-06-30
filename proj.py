from flask import Flask,jsonify, request


app = Flask(__name__)

#creating a dictionary
tasks = [
    {
        #Json format
        'Contact': 9933844961,
        'Name': u'Pranathi',
        'done': False, 
        'id': 1
    },
    {
        'Contact': 9933844932,
        'Name': u'Vaishnavi',
        'done': False, 
        'id': 2
    }
]

#Flask.route
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    #if no request is there is shows error ie u havent posted any data
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
    #here if it is posted 
    task = {
        #every task has an id..scroll up
        #and so we r creating the very next id..ie 1 more than the previous task's id
        #-1 refers to the last value in the tasks array
        #suppose that elements r with index 0 1 2
        #the data in 2 index is called -1 when counting from the right side
        'Contact': request.json['Contact'],
        'name': request.json.get('name', ""),
        'done': False,
        'id': tasks[-1]['id'] + 1
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

#__main__ is predefined 
#as soon as code is run main will....when main is running we r running the flask too
if (__name__ == "__main__"):
    app.run(debug=True)