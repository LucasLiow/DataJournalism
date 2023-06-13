# flask --app data_server run
from flask import Flask,request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f =open("data/state_crime.json","r")
    data = json.load(f)
    f.close()
    Alabama = data["Alabama"]
    years = sorted(list(Alabama.keys()))
    return render_template('index.html',years = years, data = data)
  

@app.route('/macro')
def macro():
    f =open("data/state_crime.json","r")
    data = json.load(f)
    f.close()
    numbers={}
    for state in data.keys():
        numbers[state]=data[state]["2019"]

    return render_template('macro.html', numbers = numbers)

@app.route('/micro')
def micro():
    f =open("data/state_crime.json","r")
    data = json.load(f)
    f.close()
    state = request.args.get('state')

    stateData = data[state]
    years = sorted(list(stateData.keys()))
    endpoints = []
    for i in range(len(years)-1):
        start_x = years[i] #generate endpoints for each line segment
        stop_x = years[i+1]
        endpoints.append([data[state][start_x],data[state][stop_x]])

    total = 0
    for date in data[state]:
        total += data[state][date]

    avg = total/len(data[state])
    gl = ""
    if avg >= 45950:
        gl = "higher"
    else:
        gl = "lower"
    return render_template('micro.html', state = state, endpoints = endpoints, avg = avg, gl = gl)
app.run(debug=True)
