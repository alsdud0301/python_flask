from flask import Flask, abort, jsonify, render_template, request
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
with app.app_context():
    db.create_all()
    
# 메모 생성
@app.route('/memos/create',methods=['POST'])
def create_memo():
    title = request.json['title']
    content = request.json['content']
    new_memo = Memo(title=title,content=content)
    db.session.add(new_memo)
    db.session.commit()
    return jsonify({'message': 'Memo created'}),201

@app.route('/memos',methods=['GET'])
def list_memos():
    memos = Memo.query.all()
    return jsonify([{'id':memo.id, 'title': memo.title,'content': memo.content} for memo in memos]),200

@app.route('/memos/update/<int:id>', methods=['PUT'])
def update_memo(id):
    memo = Memo.query.filter_by(id=id).first()
    if memo:
        memo.title=request.json['title']
        memo.content = request.json['content']
        db.session.commit()
        return jsonify({'message':'Memo updated'}),200
    else:
        abort(404,description="memo not found")

@app.route('/memos/delete/<int:id>', methods=['DELETE'])
def delete_memo(id):
    memo = Memo.query.filter_by(id=id).first()
    if memo:
        db.session.delete(memo)
        db.session.commit()
        return jsonify({'message': 'Memo deleted'}),200
    else:
        abort(404,description="memo not found")