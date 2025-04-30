from flask import Flask, url_for

app = Flask(__name__)

@app.route('/home')
def index():
    return "홈페이지에 오신 것을 환영합니다."

@app.route('/user/<username>')
def profile(username):
    return f'{username}님의 프로필 페이지입니다. 홈으로 가기:{url_for("index")}'

# url_for함수는 'index'라는 함수 이름으로 라우트를 찾고 해당 함수에 매핑된 최신 URL을 반환하여
# 자동으로 /home을 반환한다.