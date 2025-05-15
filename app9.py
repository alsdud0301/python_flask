from flask import Flask, request

app = Flask(__name__)

@app.route('/query')
def query_example():
    language = request.args.get('language')
    return f"Requested language: {language}"

# http://127.0.0.1:5000/query?language=python 이런 형식의 주소로 접속하게 되면
# Requested language: python이라고 응답한다. 여기서 language=python 부분이 쿼리 매개변수이다.
