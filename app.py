from flask import Flask,render_template,session, request
import sqlite3

app = Flask(__name__)

@app.route('/regist')
def regist():
    return render_template('loginform.html')
@app.route('/regist2',methods=["POST"])
def regist2():
    f_name=request.form.get("first_name")
    l_name=request.form.get("last_name")
    address=request.form.get("address")
    tel=request.form.get("tel")
    conn=sqlite3.connect('sugizaki.db')
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO meibo(first_name,last_name,address,tel) VALUES (?, ?,?,?)",
        (f_name,l_name,address,tel)
    )
    conn.commit()
    conn.close()
    return ""
@app.route('/hinban')
def hinban():
    return render_template('hinbanform.html')
@app.route('/hinban2',methods=["POST"])
def hinban2():
    hinmoku=request.form.get("hinmoku")
    genru=request.form.get("genru")
    kakaku=request.form.get("kakaku")
    meka=request.form.get("meka")
    conn=sqlite3.connect('sugizaki.db')
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO hinban(hinmoku,genru,kakaku,meka) VALUES (?, ?,?,?)",
        (hinmoku,genru,kakaku,meka)
    )
    conn.commit()
    conn.close()
    return ""
@app.route('/tyumon')
def tyumon():
    return render_template('tyumon.html')
@app.route('/tyumon2',methods=["POST"])
def tyumon2():
    hinban_id=request.form.get("hinban_id")
    kosuu=request.form.get("kosuu")
    meibo_id=request.form.get("meibo_id")
    tyumonzikakaku=request.form.get("tyumonzikakaku")
    jotai=request.form.get("jotai")
    conn=sqlite3.connect('sugizaki.db')
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO tyumon(hinban_id,kosuu,meibo_id,tyumonzikakaku,jotai)VALUES(?,?,?,?,?)",
        (hinban_id,kosuu,meibo_id,tyumonzikakaku,jotai)
    )
    conn.commit()
    conn.close()
    return ""
if __name__ =="__main__":
    app.run(debug=True)