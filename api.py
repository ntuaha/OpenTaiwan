import requests
import os
import pandas as pd
from io import StringIO
import yaml
from flask import Flask, jsonify, Response, request, send_from_directory
from flask_cors import CORS
import json

app = Flask(__name__)

PORT = 3333

# Note: Setting CORS to allow chat.openapi.com is required for ChatGPT to access your plugin
CORS(app, origins=[f"http://localhost:{PORT}", "https://chat.openai.com"])


@app.route('/.well-known/ai-plugin.json')
def serve_manifest():
    return send_from_directory(os.path.dirname(__file__), 'ai-plugin.json')


@app.route('/openapi.yaml')
def serve_openapi_yaml():
    with open(os.path.join(os.path.dirname(__file__), 'openapi.yaml'), 'r') as f:
        yaml_data = f.read()
    yaml_data = yaml.load(yaml_data, Loader=yaml.FullLoader)
    return jsonify(yaml_data)


@app.route("/logo.png")
def plugin_logo():
    return send_from_directory(os.path.dirname(__file__), 'logo.png')


@app.route("/legal")
def plugin_legal():
    return "aha rules everything!"


@app.route('/openapi.json')
def serve_openapi_json():
    return send_from_directory(os.path.dirname(__file__), 'openapi.json')


with open('data/type.json', 'r') as f:
    type_info = json.load(f)
    mapping_table = type_info['reservoir']
    mm = {m['ReservoirIdentifier']: m['ReservoirName'] for m in mapping_table}

with open('data/cs_cc_cols.json', 'r') as f:
    cs_cc_cols_info = json.load(f)


@app.route('/lists', methods=['POST'])
def lists():
    if request.is_json:
        data = request.get_json()
    else:
        print('no data')
    names = []
    if data['type_name'] == 'finance':
        names = type_info['finance']
    elif data['type_name'] == 'reservoir':
        names = [m['ReservoirName'] for m in mapping_table]

    return jsonify(names)


@app.route('/customer_support/creditcard/columns', methods=['POST'])
def cs_cc_cols():
    return jsonify(cs_cc_cols_info)


@app.route('/customer_support/creditcard', methods=['POST'])
def cs_cc():

    csv_url = "https://www.banking.gov.tw/webdowndoc?file=/stat/itopendata/banking11711.csv"

    response = requests.get(csv_url)
    response.raise_for_status()
    csv_data = StringIO(response.text)
    data_frame = pd.read_csv(csv_data)
    data_frame.columns = cs_cc_cols_info
    d = data_frame[data_frame['card issuing organization name'].isin(request.get_json()['names'])][request.get_json()['columns']].to_dict('records')
    return jsonify(d)


@app.route('/reservoirs', methods=['GET', 'POST'])
def reservoirs():

    url = 'https://data.wra.gov.tw/OpenAPI/api/OpenData/1602CA19-B224-4CC3-AA31-11B1B124530F/Data?size=100&page=0'

    if request.method == 'GET':
        response = requests.get(url, headers=headers, params=request.args)
        data = response.json()
        info = [{'WaterLevel': item['WaterLevel'] + "mm", 'RecordTime':item['ObservationTime'], 'ReservoirName':mm[item['ReservoirIdentifier']]} for item in data['responseData']]

    elif request.method == 'POST':
        print(request.headers)
        response = requests.post(url, headers=headers, params=request.args, json=request.json)
        return response.content
    else:
        raise NotImplementedError(f'Method {request.method} not implemented in wrapper for {path=}')

    return jsonify(info)


if __name__ == '__main__':
    app.run(port=PORT, host="0.0.0.0", debug=True)
