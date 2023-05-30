# flask --app data_server run
from flask import Flask,request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f =open("data/life_expectancy.json","r")
    data = json.load(f)
    f.close()

    total = 0

    can = data["Canada"]
    yearsC = sorted(list(can.keys()))

    for num in can:
       total+= can[num]

    line_endpointsC =[]
    for i in range(len(yearsC)-1): # make it easy to dynamically generate a line graph
        start_x = yearsC[i] #generate endpoints for each line segment
        stop_x = yearsC[i+1]
        line_endpointsC.append([can[start_x],can[stop_x]] )

    mex = data["Mexico"]
    yearsM = sorted(list(mex.keys()))

    for num2 in mex:
        total += mex[num2]

    line_endpointsM =[]
    for i in range(len(yearsM)-1): # make it easy to dynamically generate a line graph
        start_x = yearsM[i] #generate endpoints for each line segment
        stop_x = yearsM[i+1]
        line_endpointsM.append([mex[start_x],mex[stop_x]] )

    usa = data["United States"]
    yearsA = sorted(list(usa.keys()))

    for num3 in usa:
        total+=usa[num3]

    avg = total/(len(usa)*3)

    line_endpointsA =[]
    for i in range(len(yearsA)-1): # make it easy to dynamically generate a line graph
        start_x = yearsA[i] #generate endpoints for each line segment
        stop_x = yearsA[i+1]
        line_endpointsA.append([usa[start_x],usa[stop_x]] )

    return render_template('index.html', yearsC = yearsC, endpointsC = line_endpointsC,  yearsM = yearsM, endpointsM = line_endpointsM, yearsA = yearsA, endpointsA = line_endpointsA, avg = avg)
  

@app.route('/year')
def year():

    f =open("data/life_expectancy.json","r")
    data = json.load(f)
    f.close()

    can = data["Canada"]
    yearsC = sorted(list(can.keys()))

    mex = data["Mexico"]
    yearsM = sorted(list(mex.keys()))

    usa = data["United States"]
    yearsA = sorted(list(usa.keys()))

    year = request.args.get('year')
    return render_template('year.html', year = year, can = can, mex = mex, usa = usa)

app.run(debug=True)
