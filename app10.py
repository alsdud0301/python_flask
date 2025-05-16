from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json')
def json_example():
    # jsonify를 사용하여 JSON 형식의 응답을 반환
    return jsonify({"message": "Hello, World!"})
# http://127.0.0.1:5000/json 접속시 서버가 JSON형식의 데이터를 응답바디에 담아 반환한다.
# 여기서 jsonify() 함수는 Python 딕셔너리를 JSON 형식의 문자열로 반환하며, HTTP 응답의 Content-Type을 
# application/json으로 자동 설정해준다.


