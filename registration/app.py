from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/register', methods=['GET', 'POST']) # GET(정보보기), POST(정보수정) 메서드 허용
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        userid = request.form.get('userid')
        email = request.form.get('email')
        password = request.form.get('password')
        password_2 = request.form.get('password')
        
    if not(userid and email and password and password_2):
        return "입력되지 않은 정보가 있습니다"
    elif password != password_2:
        return "비밀번호가 일치하지 않습니다"
    else:
        usertable = User() # user_table 클래스
        usertable.userid = userid
        usertable.email = email
        usertable.password = password
        
        db.users.insert_one(userid, email, password)
        return "회원가입 성공"
    return redirect('/')



if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)