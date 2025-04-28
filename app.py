from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

# 애플리케이션 실행 시 디버그 모드 활성화
# 디버그 모드 활성화 시 개발 중 발생하는 에러 쉽게 추적가능, 수정 시 서버를 자동으로 재시작
# 운영 환경에서는 보안상의 이유로 절대 디버그 모드 활성화X
if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000)