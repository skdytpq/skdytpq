import requests
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app)
@app.route('/send_request', methods=['GET'])
def open_browser_request():
    url = "http://54.199.225.131:5001/" 
    data = {
        "gptInfo":[{"ikyKey":"ikyX1gptX1persona","keyword1":"녹차로 만든 케익"}]
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)

    return response.text  # 서버 응답을 브라우저로 반환
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True, threaded=False)