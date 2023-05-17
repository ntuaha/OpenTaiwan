import requests
import os
import pandas as pd
from io import StringIO
import yaml
from flask import Flask, jsonify, Response, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

PORT = 3333

# Note: Setting CORS to allow chat.openapi.com is required for ChatGPT to access your plugin
CORS(app, origins=[f"http://localhost:{PORT}", "https://chat.openai.com"])

#api_url = 'https://example.com'


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
    return "aha rules everythings!"

@app.route('/openapi.json')
def serve_openapi_json():
    return send_from_directory(os.path.dirname(__file__), 'openapi.json')


mapping_table = [{"ReservoirIdentifier":"10204","ReservoirName":"新山水庫","RiverName":"基隆河支流大武崙溪支流新山溪","TownName":"基隆巿安樂區"},{"ReservoirIdentifier":"10203","ReservoirName":"西勢水庫","RiverName":"基隆河支流西勢溪","TownName":"基隆巿暖暖區"},{"ReservoirIdentifier":"10205","ReservoirName":"翡翠水庫","RiverName":"新店溪支流北勢溪","TownName":"新北市新店區"},{"ReservoirIdentifier":"10302","ReservoirName":"粗坑壩","RiverName":"淡水河支流新店溪","TownName":"新北市新店區"},{"ReservoirIdentifier":"10212","ReservoirName":"直潭壩","RiverName":"淡水河支流新店溪","TownName":"新北市新店區"},{"ReservoirIdentifier":"10211","ReservoirName":"青潭堰","RiverName":"淡水河支流新店溪","TownName":"新北市新店區"},{"ReservoirIdentifier":"10214","ReservoirName":"阿玉壩","RiverName":"新店溪支流桶後溪","TownName":"新北市烏來區"},{"ReservoirIdentifier":"10213","ReservoirName":"羅好壩","RiverName":"新店溪支流南勢溪","TownName":"新北市烏來區"},{"ReservoirIdentifier":"10209","ReservoirName":"桂山壩","RiverName":"新店溪支流南勢溪","TownName":"新北市烏來區"},{"ReservoirIdentifier":"10206","ReservoirName":"榮華壩","RiverName":"淡水河支流大漢溪","TownName":"桃園市復興區"},{"ReservoirIdentifier":"10201","ReservoirName":"石門水庫","RiverName":"淡水河支流大漢溪","TownName":"桃園市龍潭區、大溪區、復興區"},{"ReservoirIdentifier":"10207","ReservoirName":"鳶山堰","RiverName":"淡水河支流大漢溪","TownName":"新北市三峽區、鶯歌區"},{"ReservoirIdentifier":"10802","ReservoirName":"羅東攔河堰","RiverName":"羅東溪","TownName":"宜蘭縣三星鄉"},{"ReservoirIdentifier":"10401","ReservoirName":"寶山水庫","RiverName":"頭前溪支流柴梳溪、頭前溪支流上坪溪(越域取水)","TownName":"新竹縣寶山鄉"},{"ReservoirIdentifier":"10405","ReservoirName":"寶山第二水庫","RiverName":"中港溪(越域取水－上坪溪)","TownName":"新竹縣寶山鄉"},{"ReservoirIdentifier":"10404","ReservoirName":"隆恩堰","RiverName":"頭前溪","TownName":"新竹縣竹東鎮、竹北市"},{"ReservoirIdentifier":"10503","ReservoirName":"大埔水庫","RiverName":"中港溪支流峨眉溪","TownName":"新竹縣峨眉鄉"},{"ReservoirIdentifier":"20510","ReservoirName":"劍潭水庫","RiverName":"中港溪支流南港溪","TownName":"苗栗縣造橋鄉"},{"ReservoirIdentifier":"10501","ReservoirName":"永和山水庫","RiverName":"中港溪支流北坑溝、中港溪支流南庄溪(越域引水)","TownName":"苗栗縣頭份市、三灣鄉"},{"ReservoirIdentifier":"10601","ReservoirName":"明德水庫","RiverName":"後龍溪支流老田寮溪","TownName":"苗栗縣頭屋鄉"},{"ReservoirIdentifier":"20101","ReservoirName":"鯉魚潭水庫","RiverName":"大安溪支流景山溪","TownName":"苗栗縣三義鄉、卓蘭鎮、大湖鄉"},{"ReservoirIdentifier":"20405","ReservoirName":"士林攔河堰","RiverName":"大安溪","TownName":"苗栗縣泰安鄉"},{"ReservoirIdentifier":"20201","ReservoirName":"德基水庫","RiverName":"大甲溪、大甲溪支流志樂溪","TownName":"臺中市和平區"},{"ReservoirIdentifier":"20207","ReservoirName":"青山壩","RiverName":"大甲溪","TownName":"臺中市和平區"},{"ReservoirIdentifier":"20203","ReservoirName":"谷關水庫","RiverName":"大甲溪、大甲溪支流小雪溪","TownName":"臺中市和平區"},{"ReservoirIdentifier":"20205","ReservoirName":"天輪壩","RiverName":"大甲溪","TownName":"臺中市和平區"},{"ReservoirIdentifier":"20206","ReservoirName":"馬鞍壩","RiverName":"大甲溪","TownName":"臺中市和平區"},{"ReservoirIdentifier":"20202","ReservoirName":"石岡壩","RiverName":"大甲溪","TownName":"臺中市石岡區"},{"ReservoirIdentifier":"20501","ReservoirName":"霧社水庫","RiverName":"濁水溪支流霧社溪","TownName":"南投縣仁愛鄉"},{"ReservoirIdentifier":"20507","ReservoirName":"武界壩","RiverName":"濁水溪支流萬大溪","TownName":"南投縣仁愛鄉"},{"ReservoirIdentifier":"20502","ReservoirName":"日月潭水庫","RiverName":"濁水溪(武界壩越域引水至水社水尾溪)","TownName":"南投縣魚池鄉"},{"ReservoirIdentifier":"20504","ReservoirName":"頭社水庫","RiverName":"濁水溪支流水里溪支流大舌滿溪","TownName":"南投縣魚池鄉"},{"ReservoirIdentifier":"20508","ReservoirName":"明湖下池水庫","RiverName":"濁水溪支流水里溪、日月潭水庫","TownName":"南投縣水里鄉"},{"ReservoirIdentifier":"20505","ReservoirName":"明潭下池水庫","RiverName":"濁水溪支流水里溪、日月潭水庫","TownName":"南投縣水里鄉"},{"ReservoirIdentifier":"20506","ReservoirName":"銃櫃壩","RiverName":"濁水溪支流水里溪支流銃櫃溪","TownName":"南投縣水里鄉"},{"ReservoirIdentifier":"20503","ReservoirName":"集集攔河堰","RiverName":"濁水溪","TownName":"南投縣集集鎮"},{"ReservoirIdentifier":"20509","ReservoirName":"湖山水庫","RiverName":"北港溪支流、清水溪","TownName":"雲林縣斗六市、古坑鄉"},{"ReservoirIdentifier":"30306","ReservoirName":"內埔子水庫","RiverName":"朴子溪","TownName":"嘉義縣民雄鄉"},{"ReservoirIdentifier":"30301","ReservoirName":"仁義潭水庫","RiverName":"八掌溪(引水渠)","TownName":"嘉義縣番路鄉"},{"ReservoirIdentifier":"30302","ReservoirName":"蘭潭水庫","RiverName":"八掌溪","TownName":"嘉義巿"},{"ReservoirIdentifier":"30303","ReservoirName":"鹿寮溪水庫","RiverName":"八掌溪支流頭前溪支流鹿寮溪","TownName":"臺南市白河區"},{"ReservoirIdentifier":"30401","ReservoirName":"白河水庫","RiverName":"急水溪支流白水溪","TownName":"臺南市白河區"},{"ReservoirIdentifier":"30402","ReservoirName":"尖山埤水庫","RiverName":"急水溪支流龜重溪上游支流","TownName":"臺南市柳營區"},{"ReservoirIdentifier":"30403","ReservoirName":"德元埤水庫","RiverName":"急水溪支流塭厝廓溪","TownName":"臺南市柳營區"},{"ReservoirIdentifier":"30501","ReservoirName":"烏山頭水庫","RiverName":"曾文溪支流官田溪、曾文溪(越域引水)","TownName":"臺南市六甲區、官田區"},{"ReservoirIdentifier":"30502","ReservoirName":"曾文水庫","RiverName":"曾文溪","TownName":"嘉義縣大埔鄉"},{"ReservoirIdentifier":"30503","ReservoirName":"南化水庫","RiverName":"曾文溪支流後堀溪、高屏溪支流旗山溪(越域引水)","TownName":"臺南市南化區"},{"ReservoirIdentifier":"30504","ReservoirName":"鏡面水庫","RiverName":"曾文溪支流菜寮溪支流鏡面溪","TownName":"臺南市南化區"},{"ReservoirIdentifier":"31002","ReservoirName":"甲仙攔河堰","RiverName":"高屏溪支流旗山溪","TownName":"高雄市甲仙區"},{"ReservoirIdentifier":"30603","ReservoirName":"玉峰堰","RiverName":"曾文溪","TownName":"臺南市山上區"},{"ReservoirIdentifier":"30602","ReservoirName":"鹽水埤水庫","RiverName":"鹽水溪支流茄苳溪","TownName":"臺南市新化區"},{"ReservoirIdentifier":"30601","ReservoirName":"虎頭埤水庫","RiverName":"鹽水溪支流茄苓崁溪","TownName":"臺南市新化區"},{"ReservoirIdentifier":"30802","ReservoirName":"阿公店水庫","RiverName":"阿公店溪、高屏溪支流旗山溪(越域引水)","TownName":"高雄市燕巢區"},{"ReservoirIdentifier":"30804","ReservoirName":"觀音湖水庫","RiverName":"後勁溪支流獅龍溪","TownName":"高雄市仁武區"},{"ReservoirIdentifier":"30805","ReservoirName":"美濃湖水庫","RiverName":"高屏溪支流荖濃溪","TownName":"高雄市美濃區"},{"ReservoirIdentifier":"30803","ReservoirName":"鳳山水庫","RiverName":"高屏溪及東港溪(越域引水)","TownName":"高雄市小港區、林園區"},{"ReservoirIdentifier":"30801","ReservoirName":"澄清湖水庫","RiverName":"高屏溪(抽水)","TownName":"高雄市鳥松區"},{"ReservoirIdentifier":"30901","ReservoirName":"高屏溪攔河堰","RiverName":"高屏溪","TownName":"高雄市大樹區、屏東縣屏東市"},{"ReservoirIdentifier":"31201","ReservoirName":"牡丹水庫","RiverName":"四重溪支流汝仍溪、牡丹溪","TownName":"屏東縣牡丹鄉"},{"ReservoirIdentifier":"31202","ReservoirName":"龍鑾潭水庫","RiverName":"(天然積水)","TownName":"屏東縣恆春鎮"},{"ReservoirIdentifier":"40101","ReservoirName":"南溪壩","RiverName":"和平南溪","TownName":"宜蘭縣南澳鄉"},{"ReservoirIdentifier":"40201","ReservoirName":"溪畔壩","RiverName":"立霧溪","TownName":"花蓮縣秀林鄉"},{"ReservoirIdentifier":"40203","ReservoirName":"龍溪壩","RiverName":"花蓮溪支流木瓜溪支流龍溪","TownName":"花蓮縣秀林鄉"},{"ReservoirIdentifier":"10215","ReservoirName":"木瓜壩","RiverName":"花蓮溪支流木瓜溪","TownName":"花蓮縣秀林鄉"},{"ReservoirIdentifier":"40202","ReservoirName":"水簾壩","RiverName":"花蓮溪支流木瓜溪","TownName":"花蓮縣秀林鄉"},{"ReservoirIdentifier":"40701","ReservoirName":"酬勤水庫","RiverName":"流麻溝","TownName":"臺東縣綠島鄉"},{"ReservoirIdentifier":"50104","ReservoirName":"赤崁地下水庫","RiverName":"赤崁村(天然積水)","TownName":"澎湖縣白沙鄉"},{"ReservoirIdentifier":"31301","ReservoirName":"成功水庫","RiverName":"港底溪及紅羅越域引水","TownName":"澎湖縣湖西鄉"},{"ReservoirIdentifier":"50102","ReservoirName":"興仁水庫","RiverName":"雙港溪支流及菜園越域引水","TownName":"澎湖縣馬公巿"},{"ReservoirIdentifier":"50103","ReservoirName":"東衛水庫","RiverName":"東衛里(天然積水)","TownName":"澎湖縣馬公巿"},{"ReservoirIdentifier":"50108","ReservoirName":"小池水庫","RiverName":"大池村(天然積水)","TownName":"澎湖縣西嶼鄉"},{"ReservoirIdentifier":"50105","ReservoirName":"西安水庫","RiverName":"西安村(天然積水)","TownName":"澎湖縣望安鄉"},{"ReservoirIdentifier":"50109","ReservoirName":"烏溝蓄水塘","RiverName":"將軍村(天然積水)","TownName":"澎湖縣望安鄉"},{"ReservoirIdentifier":"50106","ReservoirName":"七美水庫","RiverName":"東湖村(天然積水)","TownName":"澎湖縣七美鄉"},{"ReservoirIdentifier":"50204","ReservoirName":"山西水庫","RiverName":"(天然積水)","TownName":"金門縣金沙鎮"},{"ReservoirIdentifier":"50206","ReservoirName":"擎天水庫","RiverName":"金沙溪","TownName":"金門縣金沙鎮"},{"ReservoirIdentifier":"50205","ReservoirName":"榮湖水庫","RiverName":"金沙溪","TownName":"金門縣金沙鎮"},{"ReservoirIdentifier":"50207","ReservoirName":"金沙水庫","RiverName":"金沙溪","TownName":"金門縣金沙鎮"},{"ReservoirIdentifier":"50202","ReservoirName":"田浦水庫","RiverName":"前埔溪","TownName":"金門縣金沙鎮"},{"ReservoirIdentifier":"50203","ReservoirName":"陽明湖水庫","RiverName":"前埔溪","TownName":"金門縣金湖鎮"},{"ReservoirIdentifier":"50201","ReservoirName":"太湖水庫","RiverName":"山外溪","TownName":"金門縣金湖鎮"},{"ReservoirIdentifier":"50213","ReservoirName":"瓊林水庫","RiverName":"瓊林溪","TownName":"金門縣金湖鎮"},{"ReservoirIdentifier":"50214","ReservoirName":"蘭湖水庫","RiverName":"(天然積水)","TownName":"金門縣金湖鎮"},{"ReservoirIdentifier":"50212","ReservoirName":"金湖水庫","RiverName":"(天然積水)","TownName":"金門縣金湖鎮"},{"ReservoirIdentifier":"50210","ReservoirName":"西湖水庫","RiverName":"(天然積水)","TownName":"金門縣烈嶼鄉"},{"ReservoirIdentifier":"50208","ReservoirName":"蓮湖水庫","RiverName":"(天然積水)","TownName":"金門縣烈嶼鄉"},{"ReservoirIdentifier":"50209","ReservoirName":"菱湖水庫","RiverName":"(天然積水)","TownName":"金門縣烈嶼鄉"},{"ReservoirIdentifier":"50309","ReservoirName":"東湧水庫","RiverName":"(天然積水)","TownName":"連江縣東引鄉"},{"ReservoirIdentifier":"50308","ReservoirName":"坂里水庫","RiverName":"(天然積水)","TownName":"連江縣北竿鄉"},{"ReservoirIdentifier":"50302","ReservoirName":"秋桂山水庫","RiverName":"(天然積水)","TownName":"連江縣南竿鄉"},{"ReservoirIdentifier":"50305","ReservoirName":"儲水沃水庫","RiverName":"(天然積水)","TownName":"連江縣南竿鄉"},{"ReservoirIdentifier":"50307","ReservoirName":"津沙一號水庫","RiverName":"(天然積水)","TownName":"連江縣南竿鄉"},{"ReservoirIdentifier":"50306","ReservoirName":"津沙水庫","RiverName":"(天然積水)","TownName":"連江縣南竿鄉"},{"ReservoirIdentifier":"50301","ReservoirName":"勝利水庫","RiverName":"(天然積水)","TownName":"連江縣南竿鄉"},{"ReservoirIdentifier":"50310","ReservoirName":"后沃水庫","RiverName":"(天然積水)","TownName":"連江縣南竿鄉"}]
mm = {m['ReservoirIdentifier']:m['ReservoirName'] for m in mapping_table}

@app.route('/lists', methods=['POST'])
def getList():
    if request.is_json:
        data = request.get_json()
    else:
        print('no data')
    names = []
    if data['type_name']=='finance':
        names = ['三信商業銀行', '上海商業儲蓄銀行', '中國信託商業銀行', '元大商業銀行', '兆豐國際商業銀行', '日盛國際商業銀行',
        '台中商業銀行', '台北富邦商業銀行', '台新國際商業銀行', '台灣土地銀行', '臺灣中小企業銀行',
        '台灣樂天信用卡公司', '臺灣新光商業銀行', '臺灣銀行', '玉山商業銀行', '合作金庫銀行', '永豐商業銀行',
        '安泰商業銀行', '花旗（台灣）銀行', '美國運通國際股份有限公司', '?豐(台灣)商業銀行', '高雄銀行',
        '國泰世華商業銀行', '第一商業銀行', '渣打國際商業銀行', '華南商業銀行', '華泰商業銀行', '陽信商業銀行',
        '凱基商業銀行', '彰化商業銀行', '遠東國際商業銀行', '聯邦商業銀行', '星展（台灣）商業銀行']
    elif data['type_name']=='reservoir':
        names = [m['ReservoirName'] for m in mapping_table]
        
    return jsonify(names)
    


@app.route('/customer_support/creditcard/columns', methods=['POST'])
def cs_cc_cols():
    d = [
        'No',
        'Card Issuing Organization Name',
        'Accounts receivable included in the revolving credit principal, interest commencement date for each account',
'Reprinting statement fee',
'Check payment dishonored fee',
'Clearance (agency) repayment certificate fee',
'Foreign transaction settlement fee',
'Lost report fee',
'Cash advance fee',
'Review of signed transaction slip fee',
'Penalty (late processing fee)',
'Overpayment refund fee',
'Customer service phone',
'Complaint phone',
'24-hour lost report phone',
'Head office address',
'Website',
'Data update year',
'Data update month',
'Data update day'
    ]
    return jsonify(d)



@app.route('/customer_support/creditcard', methods=['POST'])
def cs():
    if request.is_json:
        print(request.get_json())
    else:
        print('lol')
    csv_url="https://www.banking.gov.tw/webdowndoc?file=/stat/itopendata/banking11711.csv"
    # Download the CSV content
    response = requests.get(csv_url)
    response.raise_for_status()

    # Read the CSV using pandas
    csv_data = StringIO(response.text)
    data_frame = pd.read_csv(csv_data)
    data_frame.columns = [
        'No',
        'Card Issuing Organization Name',
        'Accounts receivable included in the revolving credit principal, interest commencement date for each account',
'Reprinting statement fee',
'Check payment dishonored fee',
'Clearance (agency) repayment certificate fee',
'Foreign transaction settlement fee',
'Lost report fee',
'Cash advance fee',
'Review of signed transaction slip fee',
'Penalty (late processing fee)',
'Overpayment refund fee',
'Customer service phone',
'Complaint phone',
'24-hour lost report phone',
'Head office address',
'Website',
'Data update year',
'Data update month',
'Data update day'
    ]
    d = data_frame[data_frame['Card Issuing Organization Name'].isin(request.get_json()['names'])][request.get_json()['columns']].to_dict('records')
    return jsonify(d)
    

@app.route('/reservoirs', methods=['GET', 'POST'])
def wrapper():

    headers = {
    'Content-Type': 'application/json',
    }

    url = 'https://data.wra.gov.tw/OpenAPI/api/OpenData/1602CA19-B224-4CC3-AA31-11B1B124530F/Data?size=100&page=0'


    if request.method == 'GET':
        response = requests.get(url, headers=headers, params=request.args)
        data = response.json()
        info = [{'WaterLevel':item['WaterLevel']+"mm",'RecordTime':item['ObservationTime'],'ReservoirName':mm[item['ReservoirIdentifier']]} for item in data['responseData']]
    
    elif request.method == 'POST':
        print(request.headers)
        response = requests.post(url, headers=headers, params=request.args, json=request.json)
        return response.content
    else:
        raise NotImplementedError(f'Method {request.method} not implemented in wrapper for {path=}')
    
    return jsonify(info)


if __name__ == '__main__':
    app.run(port=PORT,host="0.0.0.0",debug=True)