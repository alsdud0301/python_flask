from flask import Flask

app = Flask(__name__)

@app.route('/int/<int:var>')
def int_type(var:int):
    return f'Integer : {var}'

@app.route('/float/<float:var>')
def float_type(var:float):
    return f'Float: {var}'

@app.route('/path/<path:subpath>')
def show_path(subpath):
    return f'Subpath: {subpath}'

@app.route('/uuid/<uuid:some_id>')
def show_uuid(some_id):
    return f'UUID: {some_id}'

# 플라스크의 URL타입 힌트는 타입이 일치하지 않을 경우 자동으로 404 에러를 반환하기 때문에 매개변수 검증 작업을 쉽게 처리 가능하고, 보안성도 강화할 수 있다.
