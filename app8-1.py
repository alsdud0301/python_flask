# 타입 힌트를 활용한 라우팅
# 파이썬 타입 힌트는 코드 가독성을 높이고, IDE나 린터가 실수를 미리 잡아주도록 도와준다.
def greet(name:str) -> str:
    return f"Hello, {name}"
print(greet("김민영"))

from flask import Flask
app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return 'test'
# 이 예제의 경우 /add/1/2로 접속하면 정상 작동하지만, /add/one/two로 접속 시 404에러가 발생한다.

# 플라스크에서 URL에 적용할 수 있는 타입 힌트와 파이썬에서 일반적으로 쓰는 타입 힌트는 약간 다르다.
# -string : 어떤 텍스트도 받지만 슬래시는 제외
# -int : 정수
# -float : 부동소수점 숫자
# -path : 슬래시를 포함한 문자열(<path:변수명> 형태로 지정한다.)
# -uuid : UUID 문자열(<uuid:변수명> 형태로 지정한다.)




