from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'

@app.route('/index/')
def index_con()->'html':
    return render_template('index.html')

app.run(debug=True)