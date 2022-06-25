from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps


app = Flask(__name__) # Flask 인스턴스를 생성한 것. 간단하게, app이라는 파이썬 파일을 만들었다 라는 뜻

app.config['SECRET_KEY'] = 'thisisthesecretkey'

# decorator : 다른 function을 조작하여 새로운 function을 만드는 것

def token_required(f): #token_required() : 어떤 함수 f를 받아서 그 전에 토큰 유효헝 검사를 수행해주는 decorator
    @wraps(f) 
    def decorated(*args, **kwargs):
        token = request.args.get('token') #http://127.0.0.1:5000/route?token=skjflwkejlksjgdlkj
        
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403 #Forbidden
    
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
            
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403 
            # 403 : Forbidden - 클라이언트가 해당 요청에 대한 권한이 없다고 알려주는 것
        return f(*args, **kwargs)
    
    return decorated

@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Anyone can view this!'}) 


@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'This is only available for people with valid tokens.'}) 


@app.route('/login')
def login():
    auth = request.authorization
    
    if auth and auth.password == '1234':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, app.config['SECRET_KEY']) # UTC : 협정세계시
        
        return jsonify({'token' : token})
        
    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'}) 
    # 401 : Unauthorized - 클라이언트가 인증되지 않았기 때문에 요청을 정상적으로 처리할 수 없는 상태


if __name__ == '__main__':
    app.run(debug=True)