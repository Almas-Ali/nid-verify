import requests
from flask import Flask, render_template, request, redirect
from database.models import NID
from database.register import *

app = Flask(__name__)

@app.route("/")
def nid():
    return render_template("nid_form.html")

@app.route('/nid', methods = ['POST', 'GET'])
def nid_data():
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        form_data = request.form
        req_data = {
        # "mobile" : form_data['mobile'],
        "nid" : form_data['nid'],
        "dob" : form_data['dob']
        }
        res = requests.post('https://ldtax.gov.bd/citizen/nidCheck/', data = req_data, verify=False)
        a = res.json()
        data = a['data']
        if a['success'] == 'true':
            NID.create(nid=req_data['nid'], dob=req_data['dob'])
            
        return render_template("render_nid_data.html", data = data)
     

@app.route('/list-all')
def list_all():
    list = NID.select().dicts().order_by(NID.date.desc())
    return render_template('all_nids.html', list = list)

if __name__ == '__main__':
    app.run(debug=False)
