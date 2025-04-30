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

# url_for 장점
# 1.유지보수성 : 뷰 함수의 이름이 그대로라면 url_for()가 알아서 적절한 URL을 생성해준다.
# 2.명확성 : URL 대신 뷰 함수의 이름을 사용함으로써 코드의 가독성이 향상되고, 각 링크가 어디를 지칭하는지 명확해진다.
# 3.유연성 : 뷰 함수에 정의된 변수들을 인식하고, 적절한 URL을 생성할 떄 이 변수들을 URL에 포함할 수 있다.

# 실무에서의 장점
# 1.페이지 간 내비게이션
# 2.리디렉션
# 3.자동 URL 생성
