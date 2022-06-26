import hashlib  
from pymongo import MongoClient

# DB연결
client = MongoClient('mongodb+srv://test:sparta@cluster0.sis7sux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


# 회원가입 API : id, pw, nickname를 받아서 mongoDB에 저장
# 저장하기 전에 pw를 sha256 방법(=단방향 암호화. 풀어볼 수 없다)으로 암호화해서 저장
@app.route('/api/register', methods=["POST"])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']
    
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest() # hexdigest 해시 값으로 암호화
     
    db.users.insert_one({'id': id_receive, 'pw': pw_receive, 'nick': nickname_receive})
    
    return jsonify({'result':'success'})


