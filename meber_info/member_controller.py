from flask import Flask, render_template, request, session, redirect, url_for
import mysql, mysql.connector

app = Flask(__name__)   # 웹사이트를 제작할 수 있는 객체 생성(app)
app.config["SECRET_KEY"] = "3vdTWLLW25b05EZCbd_gIQ" # Session cookie 암호화를 위해 암호키 설정

# 랜딩 페이지(index)
@app.route('/')         # 인터넷 주소를 연결해주는 곳 (URL 라우팅)
def member_info_con()->'html':
    print('Success!')
    return render_template('member_info.html')
 

# 회원 등록 페이지(register)
@app.route('/member_info_register/')
def member_info_reg_con()->'html':
    return render_template('member_info_register.html')

@app.route('/member_info_reg_model/', methods=['POST'])
def member_info_reg_model_con()->'html':
    dbconfig = {'host':'localhost', 'user':'root', 'password':'', 'database':'member_db'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    __SQl__ = """INSERT INTO member_t (name, address, email, password) VALUES (%s, %s, %s, %s)"""
    name = request.form['name']
    address = request.form['address']
    email = request.form['email']
    password = request.form['password']
    memberData = []
    memberData.append(name)
    memberData.append(address)
    memberData.append(email)
    memberData.append(password)
    print(memberData)

    cursor.execute(__SQl__, memberData)
    conn.commit()

    cursor.close()
    conn.close()

    return render_template('member_info_reg_model.html',
                            nameHtml = name,
                            addressHtml = address,
                            emailHtml = email)


# 회원 조회 페이지(search)
@app.route('/member_info_search/')
def member_info_search_con()->'html':
    return render_template('member_info_search.html')

@app.route('/member_info_search_result/', methods=['POST'])
def member_info_search_result_con()->'html':
    dbconfig = {'host':'localhost', 'user':'root', 'password':'', 'database':'member_db'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    searchName = request.form['name']
    name = (searchName, )

    __SQl__ = """SELECT * FROM member_t WHERE name=%s"""

    cursor.execute(__SQl__, name)
    row = cursor.fetchall()

    cursor.close()
    conn.close()
    
    session["USERNAME"] = row[0][1]
    print(session)

    return render_template('member_info_search_result.html',
                            nameHtml = row[0][1],
                            addressHtml = row[0][2],
                            emailHtml = row[0][3])


# 회원 정보 수정하기(update)
@app.route('/member_info_update/')
def member_info_update_con()->'html':
    if not session.get("USERNAME") is None:
        dbconfig = {'host':'localhost', 'user':'root', 'password':'', 'database':'member_db'}
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()

        name = (session.get("USERNAME"), )
        __SQL__ = """SELECT * FROM member_t WHERE name=%s"""

        cursor.execute(__SQL__, name)
        row = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('member_info_update.html',
                                nameHtml = row[0][1],
                                addressHtml = row[0][2],
                                emailHtml = row[0][3])
    else:
        return render_template('memeber_info_update.html')

@app.route('/member_info_update_result/', methods=['POST'])
def member_info_update_result_con()->'html':
    dbconfig = {'host':'localhost', 'user':'root', 'password':'', 'database':'member_db'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    __SQl__ = """UPDATE member_t SET name=%s, address=%s, email=%s WHERE name=%s"""
    newName = request.form['name']
    newAddress = request.form['address']
    newEmail = request.form['email']
    memberData = []
    memberData.append(newName)
    memberData.append(newAddress)
    memberData.append(newEmail)
    memberData.append(session.get("USERNAME"))

    cursor.execute(__SQl__, memberData)
    conn.commit()

    cursor.close()
    conn.close()
    
    session.pop("USERNAME", None)

    return render_template('member_info_search_result.html',
                            nameHtml = newName,
                            addressHtml = newAddress,
                            emailHtml = newEmail)


# 회원 정보 삭제하기(delete)
@app.route('/member_info_delete/')
def member_info_delete_con()->'html':
    return render_template('member_info_delete.html')

@app.route('/member_info_delete_prcs/', methods=['POST'])
def member_info_delete_prcs_con()->'html':
    dbconfig = {'host':'localhost', 'user':'root', 'password':'', 'database':'member_db'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    searchName = request.form['name']
    name = (searchName, )
    
    __SQl__ = """DELETE FROM member_t WHERE name=%s"""

    cursor.execute(__SQl__, name)
    conn.commit()

    cursor.close()
    conn.close()

    return render_template('member_info.html')


@app.route('/member_info_login/')
def member_info_login_con()->'html':
    if "USERNAME" in session:
        print("이미 로그인한 상태입니다.")
        return redirect(url_for("member_info_login_error_con"))
    else :
        return render_template('member_info_login.html')

@app.route('/member_info_login_result/', methods=['POST'])
def member_info_login_result_con()->'html':
    dbconfig = {'host':'localhost', 'user':'root', 'password':'', 'database':'member_db'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    inputName = request.form['name']
    inputPw = request.form['password']
    name = (inputName, )
    
    __SQl__ = """SELECT * FROM member_t WHERE name=%s"""

    cursor.execute(__SQl__, name)
    row = cursor.fetchall()
    print(row)

    cursor.close()
    conn.close()

    if row == []:
        print("등록되지 않은 회원입니다.")
        return redirect(url_for("member_info_login_con"))
    else:
        name = row[0][1]
        password = row[0][4]
        if inputPw != password:
            print("비밀번호가 맞지 않습니다.")
            return redirect(url_for("member_info_login_con"))
        else:
            print("로그인 성공")
            session["USERNAME"] = name
            print("로그인한 유저 : " + session.get("USERNAME"))
            return render_template('member_info_search_result.html',
                                    nameHtml = name,
                                    addressHtml = row[0][2],
                                    emailHtml = row[0][3])
    return render_template('member_info_login.html')

@app.route('/member_info_login_error/')
def member_info_login_error_con()->'html':
    return render_template('member_info_login_error.html')

@app.route('/member_info_logout/')
def member_info_logout_con()->'html':
    session.pop("USERNAME", None)
    print("로그아웃 성공")
    return render_template('member_info.html')

@app.route('/select_tag_test/')
def select_tag_test_con()->'html':
    return render_template('select_tag_test.html')

@app.route('/select_test/', methods=['POST'])
def select_test_con()->'html':
    field = request.form['search_field']
    data = request.form['search_data']

    return render_template('select_test.html', fieldHtml = field, dataHtml = data)

app.run(debug = True)   # Flask 내장 웹서버 실행 Port No. 5000
