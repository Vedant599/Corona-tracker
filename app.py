from flask import Flask, render_template
import requests,urllib.parse

app=Flask(__name__)

@app.route('/')
def home():
    main_api='https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise'
    json_data=requests.get(main_api).json()
    json_data=json_data['data']['statewise']
    return render_template('home.html',json_data=json_data)
@app.route('/precautions')
def precautions():
    return render_template('precautions.html')
@app.route('/helpline')
def helpline():
    return render_template('helpline.html')

@app.route('/state/<string:state>')
def state(state):
    main_api='https://api.covid19india.org/v2/state_district_wise.json'
    json_data=requests.get(main_api).json()
    return render_template('state.html',json_data=json_data,state=state)
if(__name__=='__main__'):
    app.run(debug=True)