from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/my_memo_app'
db = SQLAlchemy(app)

# 데이터 모델 정의
class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    
    def __repr__(self):
        return f'<Memo {self.title}>'
    
# 기존 라우트
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return '이것은 마이 메모 앱의 소개 페이지입니다.'

# 데이터베이스 생성
with app.app_context:
    db.create_all()