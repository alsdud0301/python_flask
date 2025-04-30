# url_for('뷰함수 이름') : 뷰 함수의 이름을 기반으로 해당 뷰 함수에 매핑된 URL을 반환한다.
# url_for('뷰함수 이름',**values) : 뷰 함수에 전달되어야 하는 변수들을 values에 '변수 = 변숫값'형태로 넣어주면 해당 변수들을 포함한 URL을 생성한다.
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

# 뷰함수
@app.route('/post/<year>/<month>/<day>')
def show_post(year,month,day):
    return f'Post for {year}/{month}/{day}'

@app.route('/')
def index():
    user_url = url_for('show_user_profile', username='johndoe')
    post_url = url_for('show_post',year='2025',month='04',day='30')
    return f'User URL : {user_url}<br>Post URL: {post_url}'

