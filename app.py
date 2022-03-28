from flask import Flask,jsonify,request

app = Flask(__name__)

datas = [
    {
        'id': 1,
        'Name': u'Raju',
        'Contact': u'9987644456', 
        'done': False
    },
    {
        'id': 1,
        'Name': u'Rohan',
        'Contact': u'9087641456', 
        'done': False
    }
]


@app.route("/add-data",methods=["POST"])

def add_tasl():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': datas[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    datas.append(datas)
    return jsonify({
        "status":"success",
        "message": "data added succesfully!"
    })
    

@app.route("/get-data")
def get_data():
    return jsonify({
        "data" : datas
    }) 

if __name__ == '__main__':
    app.run()
