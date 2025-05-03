# url_for('뷰 함수 이름',_scheme='https',_external=True) - 주로 외부 링크를 생성할 때 사용된다.

from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return f'홈 페이지 : {url_for("index")}'

# username이라는 변수를 values 매개변수로 전달하면, 플라스크는 동적 경로 /user/<username>이라는 URL을 생성한다.
@app.route('/user/<username>')
def user_profile(username):
    return f'{username}의 프로필 페이지 : {url_for("user_profile", username=username)}'

# 정적파일 style.css URL을 반환한다.
@app.route('/static-example')
def static_example():
    return f'정적 파일 URL : {url_for("static", filename="style.css")}'

# _external=True 옵션을 사용하면 도메인을 포함한 전체URL을 생성한다. 이 옵션은 외부에서 접근 가능한 URL이 필요할때 유용하다.
@app.route('/absolute')
def absolute():
    return f'외부 절대 URL: {url_for("index",_external=True)}'

# _scheme='https' 옵션은 생성되는 URL의 스키마를 지정한다. _external=True와 함께 사용하면 https를 사용하는 완전한 절대 URL을 생성한다.
# 이는 웹사이트가 SSL 인증서를 사용하여 보안을 강화한 경우 적용을 고려할 수 있다.
@app.route('/https')
def https():
    return f'HTTPS 절대 URL: {url_for("index",_scheme="https", _external=True)}'

# url_for()함수는 내부적으로 정의된 라우트에 기반하여 URL을 생성해준다.
# 이는 코드의 유지보수를 쉽게 하고, 라우트 변경이 발생해도 자동으로 반영되어 링크가 깨지는 것을 방지하는 효과가 있다.