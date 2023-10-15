from flask import Flask, render_template, request, Response
from flask import request, jsonify
from flask import Response
import requests
import os 
import openai
import argparse
import pandas as pd
from flask import make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['POST'])
def send_json_data():
    data = {
        "gtpInfo": [{
            "ikyKey": "ikyXgptXpersona",
            "keyword3": "한달간 평균 지출하는 비용은 558,911원으로서 비슷한 연령에 비하여 -10% 적은 수준입니다.",
            "keyword4": "본인 스스로에게는 소비자 응대 요인이 가장 중요하고, 동일한 연령과 성별의 소비자 유형과 비교해 보면 광고와 홍보에 가장 민감한 편입니다.",
            "keyword1": "링바인더",
            "keyword2": "친구들과 함께 즉흥적인 소비를 즐겨하며, 후기를 SNS를 통해 공유하기도 합니다.",
            "age": "10대 남성"
        }]
    }
    url = "http://54.199.225.131:5001/"

    # JSON 데이터를 POST 요청으로 전송
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return "Data sent successfully"
    else:
        return "Failed to send data"

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True,threaded=False)