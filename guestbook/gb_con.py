from flask import Flask, request, render_template, session, redirect, url_for
from db_con import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "3vdTWLLW25b05EZCbd_gIQ"

#게시판 컨트롤러
#글쓰기
@app.route('/write/')
def write_con()->'html':
    return render_template('write.html')

#글쓰기 컨트롤
@app.route('/write_db/', methods=["POST"])
def write_db_con()->'html':
    id = session.get('LOGINID')
    newName = request.form['name']
    newTitle = request.form['title']
    newContent = request.form['content']
    Db.writeContent(Db, id, newName, newTitle, newContent)

    return redirect(url_for("list_con"))

#글읽기
@app.route('/read/', methods=["GET"])
def read_con()->'html':
    no = request.args.get('no')
    Db.viewControl(Db, no)
    contentData = Db.readContent(Db, no)

    return render_template('read.html',
                            nameHtml = contentData[3],
                            titleHtml = contentData[4],
                            contentHtml = contentData[5],
                            dateHtml = contentData[6],
                            viewHtml = contentData[7])

#글목록
@app.route('/list/')
def list_con()->'html':
    return render_template('list.html', listData = Db.listContent(Db))

#글검색
@app.route('/search/', methods=["POST"])
def search_con()->'html':
    searchTarget = request.form['searchTarget']
    searchData = request.form['searchData']
    return render_template('list.html', listData = Db.searchContent(Db, searchTarget, searchData))

# 글수정
@app.route('/update/', methods=["GET", "POST"])
def update_con()->'html':
    if request.method == 'GET':
        no = request.args.get('no')
        contentData = Db.readContent(Db, no)

        return render_template('update.html',
                                noHtml = contentData[2],
                                nameHtml = contentData[3],
                                titleHtml = contentData[4],
                                contentHtml = contentData[5])
    else:
        newName = request.form['name']
        newTitle = request.form['title']
        newContent = request.form['content']
        no = request.form['no']
        Db.updateContent(Db, newName, newTitle, newContent, no)

        return redirect(url_for("read_con", no = no))

#글삭제
@app.route('/delete/', methods=["GET"])
def delete_con()->'html':
    no = request.args.get('no')
    Db.deleteContent(Db, no)
    return redirect(url_for("list_con"))

#로그인 페이지
@app.route('/login/')
def login_con()->'html':
    return render_template('login.html')

#로그인 컨트롤
@app.route('/login_db/', methods=["POST"])
def login_db_con()->'html':
    inputId = request.form['id']
    inputPw = request.form['password']
    log = Db.loginCheck(Db, inputId)

    if log is False :
        print("등록되지 않은 아이디입니다.")
    else :
        if inputPw != log :
            print("비밀번호를 잘못 입력하셨습니다.")
        else :
            print("로그인 성공!")
            session["LOGINID"] = inputId
            return redirect(url_for("list_con"))
    return redirect(url_for("login_con"))

#로그아웃
@app.route('/logout/')
def logout_con()->'html':
    session.pop("LOGINID", None)
    return redirect(url_for("list_con"))

app.run(debug = True)