from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "홈페이지에 오신 것을 환영합니다."

@app.route('/user/<username>')
def profile(username):
    # url_for()를 사용하여 'index'뷰 함수의 URL을 생성한다.
    return f'{username}님의 프로필 페이지입니다 홈으로 가기: {url_for("index")}'

# 해당파일을 실행하고 http://127.0.0.1:5000/user/join으로 접속하면
# "홈으로 가기 : /" 부분이 보이는데 이 부분이 url_for()함수에 의해 동적으로 생성된 링크이다.