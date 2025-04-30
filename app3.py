from flask import Flask, request
app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Loggin in..."
    else:
        return "Login Form"
#해당 파일을 실행시키면 GET 메서드가 기본적으로 사용되고 , Login Form이라는 글씨가 화면에 보인다