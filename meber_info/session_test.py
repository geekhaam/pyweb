from flask import Flask, render_template, request, session

app = Flask(__name__)

app.config["SECRET_KEY"] = "3vdTWLLW25b05EZCbd_gIQ" # Session cookie 암호화를 위해 암호키 설정

@app.route('/member_info_login/')
def login_con()->'html':
    session['data'] = "session data"
    print("session : " + session['data'])
    return render_template('member_info_login.html')

@app.route('/member_info_login2/')
def login_con2()->'html':
    print("session : " + session['data'])
    return render_template('member_info_login.html')

@app.route('/del_session/')
def del_sess()->'html':
    session.pop('data', None)
    return render_template('del_sess.html')

app.run(debug = True)